import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv('API_KEY')

class TrefleAPIService:
    BASE_URL = "https://trefle.io/api/v1"

    def search_plants(self, name):
        url = f"{self.BASE_URL}/plants?token={api_key}&q={name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def get_plant_detail(self, plant_id):
        url = f"{self.BASE_URL}/species/{plant_id}?token={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def search_by_family(self, family):
        url = f"{self.BASE_URL}/families?token={api_key}&q={family}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def search_by_region(self, region):
        url = f"{self.BASE_URL}/distributions/{region}?token={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
