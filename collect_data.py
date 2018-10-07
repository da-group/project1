##############################################################
# Author: DA-GROUP
# Crime Incidents in 2017: http://opendata.dc.gov/datasets/crime-incidents-in-2017
# Felony Crime Incidents in 2016: http://opendata.dc.gov/datasets/felony-crime-incidents-in-2016
# Shot Spotter Gun Shots: http://opendata.dc.gov/datasets/shot-spotter-gun-shots
# Juvenile Arrests: http://opendata.dc.gov/datasets/juvenile-arrests
##############################################################

import csv
import requests

def main():
    with open('./dataset/crime2017.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        response = requests.get('https://opendata.arcgis.com/datasets/6af5cb8dc38e4bcbac8168b27ee104aa_38.geojson').json()
        data = response['features']
        writer.writerow(data[0]['properties'].keys())
        for d in data:
            writer.writerow([d['properties'][k] for k in d['properties'].keys()])

    with open('./dataset/felony2016.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        response = requests.get('https://opendata.arcgis.com/datasets/c4164c33ab54463ab2f3585c6e9fbaf8_32.geojson').json()
        data = response['features']
        writer.writerow(data[0]['properties'].keys())
        for d in data:
            writer.writerow([d['properties'][k] for k in d['properties'].keys()])

    with open('./dataset/juvenilearrests.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        response = requests.get('https://opendata.arcgis.com/datasets/3154cd935c704e079ba56749b529a352_30.geojson').json()
        data = response['features']
        writer.writerow(data[0]['properties'].keys())
        for d in data:
            writer.writerow([d['properties'][k] for k in d['properties'].keys()])
    
    print("Data collected")

if __name__ == '__main__':
    main()