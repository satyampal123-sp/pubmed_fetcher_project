# pubmed_fetcher/__init__.py

__version__ = "0.1.0"

from .fetcher import fetch_pubmed_ids,fetch_pubmed_details
from .parser import parse_pubmed_xml
from .utils import is_non_academic
from .writer import write_to_csv

__all__ = [
    "fetch_pubmed_ids","fetch_pubmed_details",
    "parse_pubmed_xml",
    "is_non_academic",
    "write_to_csv"
]
