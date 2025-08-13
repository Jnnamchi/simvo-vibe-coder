import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.adapters import HTTPAdapter, Retry

GBIF_BASE = "https://api.gbif.org/v1"
MAX_WORKERS = 8          # tune (5–10 is usually safe)
IMG_LIMIT_DEFAULT = 15
REQ_TIMEOUT = 10         # seconds

def _build_session():
    session = requests.Session()
    retries = Retry(
        total=4,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retries, pool_connections=100, pool_maxsize=100)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({"accept": "application/json"})
    return session

def get_species_images(session: requests.Session, species_key: int, image_limit: int = IMG_LIMIT_DEFAULT):
    url = f"{GBIF_BASE}/occurrence/search"
    params = {
        "taxonKey": species_key,
        "mediaType": "StillImage",
        "limit": image_limit
    }
    try:
        r = session.get(url, params=params, timeout=REQ_TIMEOUT)
        if r.status_code != 200:
            return []
        images = []
        for occurrence in r.json().get("results", []):
            for media in occurrence.get("media", []):
                ident = media.get("identifier")
                if ident:
                    images.append(ident)
        return images
    except requests.RequestException:
        return []

def fetch_species_data(search_term, image_limit: int = IMG_LIMIT_DEFAULT):
    session = _build_session()

    # 1) Search species
    url = f"{GBIF_BASE}/species/search"
    params = {
        "datasetKey": "d7dddbf4-2cf0-4f39-9b2a-bb099caae36c",
        "q": search_term
        # You can add "limit": N here if you want to cap results
    }

    try:
        response = session.get(url, params=params, timeout=REQ_TIMEOUT)
        if response.status_code != 200:
            return {"error": f"Request failed with status code {response.status_code}"}
    except requests.RequestException as e:
        return {"error": f"Search request failed: {e}"}

    data = response.json()
    results = data.get("results", [])

    # 2) Prepare extracted items without images first
    extracted = []
    key_index = []   # store keys parallel to extracted so we can attach images after

    for item in results:
        vernacular_names = item.get("vernacularNames", [])
        vernacular_name = None
        for vn in vernacular_names:
            if vn.get("language") == "eng":
                vernacular_name = vn.get("vernacularName")
                break
        if not vernacular_name and vernacular_names:
            vernacular_name = vernacular_names[0].get("vernacularName")

        if vernacular_name:
            key = item.get("key")
            extracted_item = {
                "scientificName": item.get("scientificName", ""),
                "authorship": item.get("authorship", ""),
                "kingdom": item.get("kingdom", ""),
                "habitats": item.get("habitats", []),
                "threatStatuses": item.get("threatStatuses", []),
                "extinct": item.get("extinct", []),
                "vernacularName": vernacular_name,
                "images": []  # fill later
            }
            extracted.append(extracted_item)
            key_index.append(key)

    if not extracted:
        return []

    # 3) Fetch images concurrently for all keys we kept
    #    (If there can be duplicate keys, dedupe while keeping positions if desired)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {
            ex.submit(get_species_images, session, key, image_limit): idx
            for idx, key in enumerate(key_index)
            if key is not None
        }
        for future in as_completed(futures):
            idx = futures[future]
            try:
                images = future.result()
            except Exception:
                images = []
            extracted[idx]["images"] = images

    return extracted
