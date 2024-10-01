from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv('API_KEY')

# Now you can use the api_key variable in your code
print(f"Your API key is: {api_key}")
