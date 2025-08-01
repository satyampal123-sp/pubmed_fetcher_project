from typing import List, Dict
from xml.etree import ElementTree as ET
from .utils import is_non_academic

def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    root = ET.fromstring(xml_data)
    results = []
    for article in root.findall('.//PubmedArticle'):
        pmid = article.findtext('.//PMID')
        title = article.findtext('.//ArticleTitle')
        pub_date = article.findtext('.//PubDate/Year') or 'Unknown'
        authors_info = []
        companies = []
        email = None
        for author in article.findall('.//Author'):
            affil = author.findtext('.//AffiliationInfo/Affiliation')
            name = f"{author.findtext('ForeName', '')} {author.findtext('LastName', '')}".strip()
            if affil and is_non_academic(affil):
                authors_info.append(name)
                companies.append(affil)
            if not email and affil and '@' in affil:
                start = affil.find('@')
                parts = affil[max(0, start-30):start+30].split()
                email = next((p for p in parts if '@' in p), None)
        results.append({
            'PubmedID': pmid,
            'Title': title,
            'Publication Date': pub_date,
            'Non-academic Author(s)': '; '.join(authors_info),
            'Company Affiliation(s)': '; '.join(companies),
            'Corresponding Author Email': email or 'Not found'
        })
    return results
