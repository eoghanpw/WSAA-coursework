# assignment03-cso.py
# Program that retrieves data from the CSO and stores in a JSON file.
# Author: Eoghan Walsh
# References:
# Ref[1]: https://data.cso.ie/#
# Ref[2]: https://realpython.com/python-requests/#content
# Ref[3]: https://realpython.com/python-json/#write-a-json-file-with-python

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"


# Function to get json from cso api.
def get_cso_data(url):
    response = requests.get(url)
    return response.json()


# Function to write data to json file.
def write_cso_data(url):
    with open("cso.json", "wt") as write_file:
        json.dump(get_cso_data(url), write_file)


if __name__ == "__main__":
    write_cso_data(url)
