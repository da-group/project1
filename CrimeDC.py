import requests
import json


if __name__ == '__main__':
    re = requests.get('https://opendata.arcgis.com/datasets/6af5cb8dc38e4bcbac8168b27ee104aa_38.geojson').json()
    print(type(re))
    print(re.keys())
    print(len(re['features']))
    for i in range(10):
        print(re['features'][i])

