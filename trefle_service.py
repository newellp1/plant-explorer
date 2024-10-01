import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from the .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Access API key from environment variables
API_KEY = os.getenv('API_KEY')

# Debugging: Check if API key is loaded
print(f"API Key Loaded: {API_KEY is not None}")
print(f"API Key Value: {API_KEY}")

# Base URL for Trefle API
BASE_URL = 'https://trefle.io/api/v1'

# Define the TrefleAPIService class
class TrefleAPIService:
    def __init__(self):
        # Initialize with the base URL and the API key
        self.base_url = BASE_URL
        self.api_key = API_KEY

    # Method to search for plants by name
    def search_plants(self, plant_name):
        # Construct the API request URL
        url = f"{self.base_url}/plants?token={self.api_key}&q={plant_name}"
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            return data['data']
        else:
            print(f"Error: Unable to fetch plant data. Status code: {response.status_code}")
            return None

    # Method to get plant details by plant ID
    def get_plant_details(self, plant_id):
        url = f"{self.base_url}/species/{plant_id}?token={self.api_key}"
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: Unable to fetch plant details. Status code: {response.status_code}")
            return None

    # Method to explore plants by family ID
    def get_plants_by_family(self, family_id):
        url = f"{self.base_url}/families/{family_id}/plants?token={self.api_key}"
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            return data['data']
        else:
            print(f"Error: Unable to fetch plants by family. Status code: {response.status_code}")
            return None

    # Method to find plants by region
    def get_plants_by_region(self, region):
        url = f"{self.base_url}/distributions/{region}?token={self.api_key}"
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            return data['data']
        else:
            print(f"Error: Unable to fetch plants by region. Status code: {response.status_code}")
            return None


if __name__ == "__main__":
    trefle_service = TrefleAPIService()

    # Example 1: Search for plants by name
    print("Search for Plants by Name: 'rose'")
    plants = trefle_service.search_plants("rose")
    
    if plants:
        for plant in plants:
            print(f"Plant Name: {plant.get('common_name', 'No Common Name')}, "
                  f"Scientific Name: {plant.get('scientific_name', 'No Scientific Name')}, "
                  f"Image URL: {plant.get('image_url', 'No Image Available')}")
    else:
        print("No plants found.")

    # Example 2: View plant details by plant ID
    if plants:
        plant_id = plants[0]['id']  # Take the first plant's ID for demonstration
        print(f"\nViewing Details for Plant ID: {plant_id}")
        plant_details = trefle_service.get_plant_details(plant_id)
        if plant_details:
            print(f"Common Name: {plant_details.get('common_name', 'No Common Name')}, "
                  f"Scientific Name: {plant_details.get('scientific_name', 'No Scientific Name')}, "
                  f"Family: {plant_details.get('family', {}).get('name', 'No Family')}, "
                  f"Growth Habit: {plant_details.get('growth_habit', 'No Growth Habit')}, "
                  f"Bloom Period: {plant_details.get('bloom_period', 'No Bloom Period')}, "
                  f"Conservation Status: {plant_details.get('conservation_status', 'No Status')}, "
                  f"Image URL: {plant_details.get('image_url', 'No Image Available')}")
        else:
            print("No details found.")

    # Example 3: Explore plants by family ID
    family_id = "rosaceae"  # Replace with a valid family ID
    print(f"\nExploring Plants in Family: {family_id}")
    family_plants = trefle_service.get_plants_by_family(family_id)
    if family_plants:
        for plant in family_plants:
            print(f"Plant Name: {plant.get('common_name', 'No Common Name')}, "
                  f"Scientific Name: {plant.get('scientific_name', 'No Scientific Name')}, "
                  f"Image URL: {plant.get('image_url', 'No Image Available')}")
    else:
        print("No plants found for this family.")

    # Example 4: Find plants by region
    region = "north_america"  # Replace with a valid region
    print(f"\nFinding Plants Native to Region: {region}")
    region_plants = trefle_service.get_plants_by_region(region)
    if region_plants:
        for plant in region_plants:
            print(f"Plant Name: {plant.get('common_name', 'No Common Name')}, "
                  f"Scientific Name: {plant.get('scientific_name', 'No Scientific Name')}, "
                  f"Region: {plant.get('native', {}).get('region', 'No Region')}, "
                  f"Image URL: {plant.get('image_url', 'No Image Available')}")
    else:
        print("No plants found for this region.")
