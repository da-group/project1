##############################################################
# Author: DA-GROUP
# data source: http://opendata.dc.gov/datasets/crime-incidents-in-2017?page=9
##############################################################


import csv
import requests


if __name__ == '__main__':
    with open('./dataset/crime2017.csv', 'w') as f:
        writer = csv.writer(f)
        response = requests.get('https://opendata.arcgis.com/datasets/6af5cb8dc38e4bcbac8168b27ee104aa_38.geojson').json()
        data = response['features']
        writer.writerow(data[0]['properties'].keys())
        for d in data:
            writer.writerow([d['properties'][k] for k in d['properties'].keys()])

