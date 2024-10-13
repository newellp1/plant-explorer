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
1. When searching for plants by name and attempting to retrieve details by plant ID, the detailed information (such as common name, scientific name, family, etc.) was returning N/A for many fields.

Cause: The get_plant_details method was using the wrong endpoint (/species/{plant_id}), and some fields were not present in the API response.

Fix: The endpoint was updated to /plants/{plant_id} to correctly retrieve the plant details. Safe access with .get() was used to handle potentially missing data.

2. Even after fixing the endpoint, some fields (like family, genus, and conservation status) were still returning N/A, and we suspected incorrect parsing of the JSON response.

Cause: The structure of the API response was different than expected, with nested dictionaries and missing fields for some plants.

Fix: Added print statements to debug the raw API response. Used safe dictionary lookups (.get()) to avoid KeyErrors and handle missing data gracefully.

3. When attempting to print species information, an AttributeError occurred because the species field was a list, not a dictionary.

Cause: The code incorrectly assumed species was a dictionary and used .get(), which caused the error when the field was a list.

Fix: The species field was handled as a list, and a loop was added to iterate over the species list to print the scientific names of all species in the response.

4. An error was encountered when attempting to run main.py with an invalid command (ps/python3.12.exe).

Cause: Incorrect path or typo in the command.

Fix: The correct command (python main.py or python3 main.py) was used to run the script, ensuring that Python was executed from the correct directory.

5. Some fields were still missing after fixing the endpoint and data parsing logic.

Cause: The Trefle API may not return all data fields for every plant.

Fix: Continued using safe dictionary access with .get(), allowing for missing fields to return N/A rather than causing errors.

6. To ensure the application behaves correctly across various API responses, additional debugging was added to inspect raw responses, and error handling was improved.

Fix: Added print statements for raw API responses and used .get() for all dictionary lookups to avoid errors caused by missing fields.

7. When selecting "Exit" in the main menu, the program does not exit as expected and the menu is displayed again.

Cause: The self.main_menu() method weas incorrectly being called in the view_plants_by_family, search_plants_by_region, and view_plant_details methods, causing the menu to loop indefinitely.

Fix: Removed the unnecessary self.main_menu() calls from these methods.  Now, the main_menu() method itself handles manu navigation or exiting.

## GitHub Workflow for Fixes:
1. Frequent commits were made to track changes and fixes.
2. All changes were staged, committed with descriptive messages, and pushed to the remote GitHub repository.

## Commit Messages Used:
"Updated PlantExplorer and TrefleAPIService to include API response debugging"
"Fixed species handling in PlantExplorer and added safe access for API data"
"Corrected endpoint for fetching plant details and improved error handling"
"Handled list format for species field to avoid AttributeError"