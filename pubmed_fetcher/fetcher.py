import requests
from typing import List
from xml.etree import ElementTree as ET

def fetch_pubmed_ids(query: str, retmax: int = 20) -> List[str]:
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    params = {'db': 'pubmed', 'term': query, 'retmode': 'xml', 'retmax': retmax}
    response = requests.get(url, params=params)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    return [id_elem.text for id_elem in root.findall('.//Id')]

def fetch_pubmed_details(ids: List[str]) -> str:
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    params = {'db': 'pubmed', 'id': ','.join(ids), 'retmode': 'xml'}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text
