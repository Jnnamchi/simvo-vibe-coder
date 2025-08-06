import json
import requests

import requests

def get_species_images(species_key, image_limit=3):
    print("Getting ... " + str(species_key))
    url = "https://api.gbif.org/v1/occurrence/search"
    params = {
        "taxonKey": species_key,
        "mediaType": "StillImage",
        "limit": image_limit
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []

    images = []
    for occurrence in response.json().get("results", []):
        for media in occurrence.get("media", []):
            images.append(media.get("identifier"))
    return images

# Define the URL and headers
url = 'https://api.gbif.org/v1/species/search'
params = {
    'datasetKey': 'd7dddbf4-2cf0-4f39-9b2a-bb099caae36c',
    'q': 'kangaroo'
}
headers = {
    'accept': 'application/json'
}

# Send GET request
response = requests.get(url, headers=headers, params=params)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    results = data.get('results', [])
    
    # Extract selected keys
    extracted = []
    for item in results:
        
        # Extract vernacular name based on priority
        vernacular_names = item.get('vernacularNames', [])
        vernacular_name = None

        for vn in vernacular_names:
            if vn.get('language') == 'eng':
                vernacular_name = vn.get('vernacularName')
                break
        if not vernacular_name and vernacular_names:
            vernacular_name = vernacular_names[0].get('vernacularName')

        if vernacular_name:
            key = item.get('key', '')
            extracted_item = {
                'scientificName': item.get('scientificName', ''),
                'authorship': item.get('authorship', ''),
                'kingdom': item.get('kingdom', ''),
                'habitats': item.get('habitats', []),
                'threatStatuses': item.get('threatStatuses', []),
                'extinct': item.get('extinct', []),
                'vernacularName': vernacular_name,
                'images': get_species_images(key)
            }
            extracted.append(extracted_item)

    # Print the extracted data
    print(json.dumps(extracted, indent=2))

else:
    print(f"Request failed with status code {response.status_code}")