import urllib.request
import json

print("--- LIGO Gravitational Wave Event Metadata Fetcher ---")

event_url = "https://gwosc.org/api/v2/event-versions/GW150914-v3"

try:
    req = urllib.request.Request(
        event_url, 
        headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
    )
    response = urllib.request.urlopen(req)
    data = json.loads(response.read().decode())
    
    print("Successfully connected to LIGO Open Science Center (GWOSC) API v2.")
    print(f"Event: {data.get('name')} | Catalog: {data.get('catalog')}")
    print(f"GPS Merger Time: {data.get('gps')} | Detectors: {', '.join(data.get('detectors', []))}")
    print(f"Official DOI: {data.get('doi')}")
    
except Exception as e:
    print(f"API connection status: {e}")
