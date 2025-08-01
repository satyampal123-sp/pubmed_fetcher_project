from pubmed_fetcher.fetcher import fetch_pubmed_ids, fetch_pubmed_details
from pubmed_fetcher.parser import parse_pubmed_xml
from pubmed_fetcher.writer import write_to_csv
import argparse

def main():
    parser = argparse.ArgumentParser(description='Fetch PubMed papers')
    parser.add_argument('query')
    parser.add_argument('-f', '--file')
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()

    ids = fetch_pubmed_ids(args.query)
    if args.debug:
        print(f"Fetched IDs: {ids}")
    xml_data = fetch_pubmed_details(ids)
    results = parse_pubmed_xml(xml_data)
    if args.file:
        write_to_csv(args.file, results)
    else:
        for r in results:
            print(r)

if __name__ == '__main__':
    main()
