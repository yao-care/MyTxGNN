"""Data collectors for evidence gathering."""

from .base import BaseCollector, CollectorResult
from .clinicaltrials import ClinicalTrialsCollector
from .drugbank import DrugBankCollector
from .ictrp import ICTRPCollector
from .npra import NPRACollector
from .pubmed import PubMedCollector

__all__ = [
    "BaseCollector",
    "ClinicalTrialsCollector",
    "CollectorResult",
    "DrugBankCollector",
    "ICTRPCollector",
    "NPRACollector",
    "PubMedCollector",
]
