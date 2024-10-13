import requests
from dotenv import load_dotenv
import os

class TrefleAPIService:
    def __init__(self):
        # Load the environment variables
        load_dotenv()
        self.api_key = os.getenv('API_KEY')
    
    def search_plants_by_name(self, plant_name):
        url = f"https://trefle.io/api/v1/plants?token={self.api_key}&q={plant_name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(f"Error: {response.status_code}")
            return None

    def explore_plants_by_family(self, family_name):
        url = f"https://trefle.io/api/v1/families/{family_name}/plants?token={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(f"Error: {response.status_code}")
            return None

    def search_plants_by_region(self, region_name):
        url = f"https://trefle.io/api/v1/distributions/{region_name}/plants?token={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(f"Error: {response.status_code}")
            return None

    def get_plant_details(self, plant_id):
        # Use the 'plants' endpoint instead of 'species' to get details based on plant ID
        url = f"https://trefle.io/api/v1/plants/{plant_id}?token={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['data']  # Ensure you're accessing the 'data' part of the JSON
        else:
            print(f"Error: {response.status_code}")
            return None
