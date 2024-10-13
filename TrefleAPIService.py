import requests
from dotenv import load_dotenv
import os

class TrefleAPIService:
    def __init__(self):
        # Load the environment variables
        load_dotenv()
        self.api_key = os.getenv('API_KEY')
        if not self.api_key:
            raise ValueError("API Key not found. Please check your .env file.")

    def search_plants_by_name(self, plant_name):
        url = f"https://trefle.io/api/v1/plants?token={self.api_key}&q={plant_name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('data', [])
        else:
            print(f"Error {response.status_code}: Unable to search for plants by name.")
            return None

    def explore_plants_by_family(self, family_name):
        url = f"https://trefle.io/api/v1/plants?token={self.api_key}&filter[family]={family_name}"
        
        # Make the API request
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json().get('data', [])
        else:
            print(f"Error {response.status_code}: Unable to explore plants by family '{family_name}'.")
        
        return None

    def search_plants_by_region(self, region_name):
        url = f"https://trefle.io/api/v1/plants?token={self.api_key}&filter[distributions]={region_name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('data', [])
        else:
            print(f"Error {response.status_code}: Unable to search for plants by region '{region_name}'.")
            return None

    def get_plant_details(self, plant_id):
        url = f"https://trefle.io/api/v1/plants/{plant_id}?token={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('data', {})
        else:
            print(f"Error {response.status_code}: Unable to retrieve plant details for ID '{plant_id}'.")
            return None
