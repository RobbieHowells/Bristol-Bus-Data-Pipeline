import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("BODS_API_KEY")
if api_key is None:
    raise ValueError("BODS_API_Key is not set")

url = "https://data.bus-data.dft.gov.uk/api/v1/datafeed/"

params = {
    "api_key": api_key,
    "boundingBox": "-2.72,51.35,-2.45,51.57"
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

filename = "vehicle_locations_" + timestamp + ".xml"

filepath = os.path.join("data", "raw", filename)

with open(filepath, "wb") as raw_data:
    raw_data.write(response.content)