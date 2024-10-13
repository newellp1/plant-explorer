# Plant Explorer

Plant Explorer is a Python application that interacts with the Trefle API to search for plants, view plant details, and explore plants by family or region.

## Features
- Search for plants by name
- View detailed information for specific plants
- Explore plants by family
- Find plants based on geographical regions
- Display plant images

## Requirements
- Python 3.9 or higher
- Requests library
- python-dotenv for loading API keys

## Installation
1. Clone the repository or upload files to your desired environment (e.g., PythonAnywhere).
2. Install dependencies by running:
   ```bash
   pip install -r requirements.txt


## Issues
The search functionality is working fine but the result is pulling a bunch of plant common names and thier scientific names and not the one that I had searched for.  However, when I attempt to retrieve the details for a specific plant by its ID, the results for common name, scientific name, family, and other fields are not being populated correctly.
