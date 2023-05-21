import requests
from tqdm import tqdm

input_file = 'output.txt'
output_file = 'final_parcel.txt'

with open(input_file, 'r') as file:
    lines = file.readlines()

with open(output_file, 'a') as file:
    for line in tqdm(lines, desc='Fetching parcels', unit='parcel'):
        parcel_number = line.strip()
        url = f'https://atip.piercecountywa.gov/api/pcAtipSummary?iParcelNumber={parcel_number}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'max-age=0, must-revalidate',
            'DNT': '1',
            'Connection': 'keep-alive'
        }

        response = requests.get(url, headers=headers)
        file.write(response.text + '\n')
