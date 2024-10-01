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
        
        # Make the API request
        response = requests.get(url)

        # Print the response status code for debugging
        print(f"Status Code: {response.status_code}")
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            print(data)  # Print the full response for debugging
            return data['data']  # Return the list of plants
        else:
            print(f"Error: Unable to fetch plant data. Status code: {response.status_code}")
            return None


if __name__ == "__main__":
    trefle_service = TrefleAPIService()

    # Test searching for plants
    print("Testing API call for plant 'rose'")
    plants = trefle_service.search_plants("rose")
    
    if plants:
        for plant in plants:
            # Print common name, scientific name, and image URL
            print(f"Plant Name: {plant['common_name']}, Scientific Name: {plant['scientific_name']}, Image URL: {plant.get('image_url', 'No Image Available')}")
    else:
        print("No plants found.")
