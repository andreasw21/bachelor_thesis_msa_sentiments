import json
import requests


def get_json_from(url: str) -> json:
    """
    Fetches JSON data from a given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
