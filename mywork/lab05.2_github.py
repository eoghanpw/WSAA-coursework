# Script to get info from private github repo.
# Author: Eoghan Walsh

import requests
from config import config as cfg
import json

url = "https://api.github.com/repos/eoghanpw/aprivateone"

api_key = cfg["githubkey"]

response = requests.get(url, auth=("token", api_key))

repo_json = response.json()

with open("private_repo.json", "w") as fp:
    json.dump(repo_json, fp, indent=4)
