import csv
from typing import List, Dict

def write_to_csv(filename: str, data: List[Dict]) -> None:
    if not data:
        print('No data to write.')
        return
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
