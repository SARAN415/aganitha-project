import requests
import xml.etree.ElementTree as ET
import re
from typing import List, Dict, Optional

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_pubmed_ids(query: str, max_results: int = 10) -> List[str]:
    """
    Fetch PubMed IDs based on a search query.
    :param query: The search term for PubMed.
    :param max_results: Maximum number of results to fetch.
    :return: A list of PubMed IDs.
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(PUBMED_SEARCH_URL, params=params)
    
    if response.status_code != 200:
        raise Exception("Error fetching PubMed IDs")
    
    return response.json().get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(pubmed_id: str) -> Optional[Dict[str, str]]:
    """
    Fetches details of a specific PubMed paper.
    :param pubmed_id: The unique identifier for a PubMed paper.
    :return: Dictionary containing paper details.
    """
    params = {
        "db": "pubmed",
        "id": pubmed_id,
        "retmode": "xml"
    }
    
    response = requests.get(PUBMED_FETCH_URL, params=params)
    
    """Error"""
    if response.status_code != 200:
        return None
    
    root = ET.fromstring(response.text)
    
    title = root.find(".//ArticleTitle")
    pub_date = root.find(".//PubDate/Year")
    
    authors = []
    companies = []
    
    for author in root.findall(".//Author"):
        affiliation = author.find("Affiliation")
        last_name = author.find("LastName")
        
        if affiliation is not None and last_name is not None:
            if re.search(r"(Pharma|Biotech|Inc|Ltd)", affiliation.text, re.IGNORECASE):
                authors.append(last_name.text)
                companies.append(affiliation.text)
    
    return {
        "PubmedID": pubmed_id,
        "Title": title.text if title is not None else "N/A",
        "Publication Date": pub_date.text if pub_date is not None else "N/A",
        "Non-academic Author(s)": ", ".join(authors),
        "Company Affiliation(s)": ", ".join(companies),
        "Corresponding Author Email": "N/A"
    }
