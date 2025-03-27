import argparse
import csv
from typing import List, Dict
from pubmed_api import fetch_pubmed_ids, fetch_paper_details

def save_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    """
    Saves the extracted paper details to a CSV file.

    :param data: List of dictionaries containing paper details.
    :param filename: Name of the output CSV file.
    """
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Results saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    pubmed_ids = fetch_pubmed_ids(args.query)

    results = []
    for pubmed_id in pubmed_ids:
        details = fetch_paper_details(pubmed_id)
        if details:
            results.append(details)
    
    if args.file:
        save_to_csv(results, args.file)
    else:
        for result in results:
            print(result)

if __name__ == "__main__":
    main()
