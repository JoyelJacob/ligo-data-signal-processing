import urllib.request
import json
import numpy as np

print("--- LIGO Gravitational Wave Data Downloader ---")

event_url = "https://gwosc.org"

try:
    response = urllib.request.urlopen(event_url)
    data = json.loads(response.read().decode())
    
    strain_file_url = data['events']['GW150914-v3']['strain']['url']
    print(f"Successfully found LIGO data packet link:\n{strain_file_url}")
    print("\nNext Step: Run data analysis via SciPy / NumPy arrays.")
    
except Exception as e:
    print(f"Error accessing LIGO Open Science API: {e}")
