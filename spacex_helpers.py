import requests
import pandas as pd

def get_lookup_dict(url, id_key='id', value_key='name'):
    response = requests.get(url)
    if response.status_code == 200:
        items = response.json()
        return {item[id_key]: item[value_key] for item in items}
    else:
        print(f"❌ Error fetching {url}")
        return {}