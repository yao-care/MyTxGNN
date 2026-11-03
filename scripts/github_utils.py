#!/usr/bin/env python3
"""
GitHub API utilities for EuTxGNN evidence checking scripts.
Provides deduplication and issue management functions.
"""

import os
import re
from typing import Optional, List

import requests

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/MyTxGNN")


def get_headers() -> dict:
    """Get GitHub API headers (no Authorization header without a token: read-only public access)."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


# 2026-11-03：issue 列表一律分頁取全部（原本只看前 100 筆，積壓超過 100 筆後去重與 close-older 都失效）
def list_issues(labels: str, state: str = "open") -> List[dict]:
    """List all issues (not PRs) with the given labels (comma-separated = AND), following pagination."""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    params = {"state": state, "labels": labels, "per_page": 100, "page": 1}
    issues = []
    while True:
        response = requests.get(url, headers=get_headers(), params=params, timeout=30)
        response.raise_for_status()
        batch = response.json()
        issues.extend(i for i in batch if "pull_request" not in i)
        if len(batch) < 100 or 'rel="next"' not in response.headers.get("Link", ""):
            break
        params["page"] += 1
    return issues


# 監測 issue 標題「<emoji> <類型>: <藥名> (<數量> …) → <預測>」；半形「:」與全形「：」都接受
TITLE_DRUG_RE = re.compile(r"[:：]\s*(.+?)\s*\(\d+")


def title_drug_name(title: str) -> Optional[str]:
    match = TITLE_DRUG_RE.search(title or "")
    return match.group(1).strip() if match else None


_KNOWN_TITLES = None  # 本次執行內快取所有 auto-detected issue 標題（含 closed），避免每開一筆就重抓全部分頁


def issue_exists(title: str, state: str = "all") -> bool:
    """
    Check if an issue with the given title already exists.

    Args:
        title: The exact issue title to search for
        state: "open", "closed", or "all" (default: "all")

    Returns:
        True if an issue with this title exists, False otherwise
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would check for existing issue: {title}")
        return False

    global _KNOWN_TITLES
    try:
        if state != "all":
            titles = {i.get("title"): i["number"] for i in list_issues("auto-detected", state=state)}
        else:
            if _KNOWN_TITLES is None:
                _KNOWN_TITLES = {i.get("title"): i["number"] for i in list_issues("auto-detected", state="all")}
            titles = _KNOWN_TITLES
        if title in titles:
            print(f"  → Issue already exists: #{titles[title]} - {title}")
            return True
        return False

    except requests.RequestException as e:
        print(f"Warning: Could not check for existing issues: {e}")
        return False


def find_existing_issues_by_label(drug_name: str, label: str, state: str = "open") -> List[dict]:
    """
    Find existing issues for a specific drug with a given label.

    Args:
        drug_name: The drug name to search for
        label: The label to filter by (e.g., "pubmed", "clinicaltrials")
        state: "open", "closed", or "all" (default: "open")

    Returns:
        List of matching issues (sorted by number, newest first)
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would search for {label} issues: {drug_name}")
        return []

    try:
        issues = list_issues(label, state=state)

        # Filter issues matching the drug name pattern
        # Title formats（藥名後面是「(數量」，之後可能接「→ 預測」）:
        # - 📚 New Publications: DrugName (N papers) → indication
        # - 🔬 New Clinical Trials: DrugName (N trials) → indication
        matching = []
        drug_name_lower = drug_name.lower()
        for issue in issues:
            issue_drug = title_drug_name(issue.get("title", ""))
            if issue_drug and issue_drug.lower() == drug_name_lower:
                matching.append({
                    "number": issue["number"],
                    "title": issue["title"],
                    "url": issue["html_url"]
                })

        # Sort by issue number (newest first)
        matching.sort(key=lambda x: x["number"], reverse=True)
        return matching

    except requests.RequestException as e:
        print(f"Warning: Could not search for existing issues: {e}")
        return []


def close_issue(issue_number: int, comment: str = None, state_reason: str = None) -> bool:
    """
    Close a GitHub issue with an optional comment.

    Args:
        issue_number: The issue number to close
        comment: Optional comment to add before closing
        state_reason: Optional "completed" / "not_planned"

    Returns:
        True if successful, False otherwise
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would close issue #{issue_number}")
        return True

    try:
        # Add comment if provided
        if comment:
            comment_url = f"https://api.github.com/repos/{GITHUB_REPO}/issues/{issue_number}/comments"
            requests.post(comment_url, headers=get_headers(), json={"body": comment}, timeout=30).raise_for_status()

        # Close the issue
        url = f"https://api.github.com/repos/{GITHUB_REPO}/issues/{issue_number}"
        payload = {"state": "closed"}
        if state_reason:
            payload["state_reason"] = state_reason
        response = requests.patch(url, headers=get_headers(), json=payload, timeout=30)
        response.raise_for_status()
        print(f"  → Closed issue #{issue_number}")
        return True

    except requests.RequestException as e:
        print(f"Error closing issue #{issue_number}: {e}")
        return False


def close_older_issues_by_label(drug_name: str, label: str, issue_type: str) -> int:
    """
    Close older issues for a drug with a specific label, keeping only the latest.

    Args:
        drug_name: The drug name to process
        label: The label to filter by (e.g., "pubmed", "clinicaltrials")
        issue_type: Human-readable description for the comment

    Returns:
        Number of issues closed
    """
    existing = find_existing_issues_by_label(drug_name, label, state="open")

    if len(existing) <= 1:
        return 0

    # Keep the first (newest), close the rest
    closed_count = 0
    for issue in existing[1:]:
        comment = f"🤖 Auto-closed: Newer issue #{existing[0]['number']} now tracks this drug's {issue_type}."
        if close_issue(issue["number"], comment):
            closed_count += 1

    return closed_count


def close_older_pubmed_issues(drug_name: str) -> int:
    """Close older PubMed issues for a drug."""
    return close_older_issues_by_label(drug_name, "pubmed", "publications")


def close_older_clinicaltrials_issues(drug_name: str) -> int:
    """Close older ClinicalTrials issues for a drug."""
    return close_older_issues_by_label(drug_name, "clinicaltrials", "clinical trials")


def create_issue(title: str, body: str, labels: list) -> Optional[str]:
    """
    Create a GitHub issue with deduplication check.

    Args:
        title: Issue title
        body: Issue body (markdown)
        labels: List of label names

    Returns:
        Issue URL if created, None if skipped or failed
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would create issue: {title}")
        return None

    # Check if issue already exists
    if issue_exists(title):
        print(f"  → Skipping duplicate issue: {title}")
        return None

    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    payload = {
        "title": title,
        "body": body,
        "labels": labels
    }

    try:
        response = requests.post(url, headers=get_headers(), json=payload, timeout=30)
        response.raise_for_status()
        issue_url = response.json().get("html_url")
        if _KNOWN_TITLES is not None:
            _KNOWN_TITLES[title] = response.json().get("number")
        print(f"  → Created issue: {issue_url}")
        return issue_url

    except requests.RequestException as e:
        print(f"Error creating issue: {e}")
        return None
