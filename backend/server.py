import os
import requests
import csv

from dotenv import load_dotenv

load_dotenv()

source = os.getenv("SOURCE")
source_location = os.getenv("SOURCELOCATION")

def download_csv():
    try:
        response = requests.get(source)
        response.raise_for_status()

        csv_data = response.text

        with open(source_location, 'w') as csv_file:
            csv_file.write(csv_data)

        print('CSV file downloaded successfully!')
    except requests.exceptions.RequestException as error:
        print('Error downloading CSV:', error)

def load_csv():
    if os.path.exists(source_location):
        with open(source_location, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)

        print('CSV file parsed successfully.')
    else:
        print('Source does not exist')

if __name__ == "__main__":
    download_csv()