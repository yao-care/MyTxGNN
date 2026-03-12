"""Malaysia NPRA (National Pharmaceutical Regulatory Agency) collector.

Searches the local Malaysia FDA drug database for drug information.
Data source: https://data.gov.my/data-catalogue/pharmaceutical_products
"""

import json
import re
from pathlib import Path
from typing import Any

from .base import BaseCollector, CollectorResult


class NPRACollector(BaseCollector):
    """Collector for Malaysia NPRA drug registration data.

    Searches the locally cached NPRA drug database (my_fda_drugs.json)
    for drug registration information.
    """

    source_name = "npra"

    def __init__(self, data_path: Path | str | None = None):
        """Initialize the collector.

        Args:
            data_path: Path to the my_fda_drugs.json file.
                      If None, uses default location.
        """
        if data_path is None:
            data_path = (
                Path(__file__).parent.parent.parent.parent
                / "data"
                / "raw"
                / "my_fda_drugs.json"
            )
        self.data_path = Path(data_path)
        self._data: list[dict] | None = None

    def _load_data(self) -> list[dict]:
        """Load the NPRA data from JSON file."""
        if self._data is None:
            if not self.data_path.exists():
                raise FileNotFoundError(
                    f"NPRA data file not found: {self.data_path}"
                )
            with open(self.data_path, encoding="utf-8") as f:
                self._data = json.load(f)
        return self._data

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search for drug registrations in Malaysia.

        Args:
            drug: Drug name (ingredient or product name)
            disease: Not used (NPRA data doesn't include indications)

        Returns:
            CollectorResult with matching drug registrations
        """
        query = {"drug": drug, "disease": disease}

        try:
            data = self._load_data()
            matches = self._search_drugs(data, drug)

            return self._make_result(
                query=query,
                data=matches,
                success=True,
            )

        except Exception as e:
            return self._make_result(
                query=query,
                data=[],
                success=False,
                error_message=str(e),
            )

    def _search_drugs(self, data: list[dict], drug: str) -> list[dict]:
        """Search for drugs matching the query.

        Args:
            data: List of drug records
            drug: Drug name to search for

        Returns:
            List of matching drug records
        """
        matches = []
        drug_lower = drug.lower()
        drug_pattern = re.compile(re.escape(drug_lower), re.IGNORECASE)

        for record in data:
            # Search in product name
            product = str(record.get("product", "") or "")
            # Search in active ingredients
            ingredients = str(record.get("active_ingredient", "") or "")
            # Search in generic name
            generic = str(record.get("generic_name", "") or "")
            # Search in normalized ingredients
            normalized = str(record.get("ingredients_normalized", "") or "")

            if (
                drug_pattern.search(product)
                or drug_pattern.search(ingredients)
                or drug_pattern.search(generic)
                or drug_pattern.search(normalized)
            ):
                matches.append(self._format_record(record))

        return matches

    def _format_record(self, record: dict) -> dict:
        """Format a drug record for output.

        Args:
            record: Raw drug record from JSON

        Returns:
            Formatted drug record
        """
        return {
            "registry": "NPRA Malaysia",
            "reg_no": record.get("reg_no", ""),
            "product": record.get("product", ""),
            "active_ingredient": record.get("active_ingredient", ""),
            "generic_name": record.get("generic_name", ""),
            "holder": record.get("holder", ""),
            "description": record.get("description", ""),
            "status": record.get("status", ""),
            "date_reg": record.get("date_reg", ""),
            "date_end": record.get("date_end", ""),
            "url": f"https://npra.gov.my/index.php/search/product/{record.get('reg_no', '')}",
        }

    def get_drug_by_reg_no(self, reg_no: str) -> dict | None:
        """Get drug details by registration number.

        Args:
            reg_no: NPRA registration number

        Returns:
            Drug record or None if not found
        """
        try:
            data = self._load_data()
            for record in data:
                if record.get("reg_no") == reg_no:
                    return self._format_record(record)
            return None
        except Exception:
            return None

    def get_drugs_by_ingredient(self, ingredient: str) -> list[dict]:
        """Get all drugs containing a specific ingredient.

        Args:
            ingredient: Active ingredient name

        Returns:
            List of matching drug records
        """
        try:
            data = self._load_data()
            return self._search_drugs(data, ingredient)
        except Exception:
            return []

    def get_statistics(self) -> dict:
        """Get statistics about the NPRA database.

        Returns:
            Dictionary with database statistics
        """
        try:
            data = self._load_data()
            statuses = {}
            descriptions = {}

            for record in data:
                status = record.get("status", "Unknown")
                desc = record.get("description", "Unknown")
                statuses[status] = statuses.get(status, 0) + 1
                descriptions[desc] = descriptions.get(desc, 0) + 1

            return {
                "total_records": len(data),
                "by_status": statuses,
                "by_description": descriptions,
            }
        except Exception as e:
            return {"error": str(e)}
