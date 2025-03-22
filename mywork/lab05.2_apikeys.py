# Script that will convert website into pdf.
# Author: Eoghan Walsh

import requests
import urllib.parse
from config import config as cfg

target_url = "https://html2pdf.app/documentation"

api_key = cfg["html2pdfkey"]

api_url = "https://api.html2pdf.app/v1/generate"

params = {"html": target_url, "apiKey": api_key}
parsed_params = urllib.parse.urlencode(params)
request_url = api_url + "?" + parsed_params

response = requests.get(request_url)
print(response.status_code)

pdf = response.content
with open("html2pdf.pdf", "wb") as handler:
    handler.write(pdf)
