class PlantExplorer:
    def __init__(self, api_service):
        self.api_service = api_service

    def main_menu(self):
        while True:
            print("--- Plant Explorer ---")
            print("1. Search Plants by Name")
            print("2. View Plants by Family")
            print("3. Search Plants by Region")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.search_plants()
            elif choice == "2":
                self.view_plants_by_family()
            elif choice == "3":
                self.search_plants_by_region()
            elif choice == "4":
                print("Exiting Plant Explorer...")
                break
            else:
                print("Invalid choice. Please try again.")

    def search_plants(self):
        plant_name = input("Enter plant name: ")
        results = self.api_service.search_plants_by_name(plant_name)

        if results:
            for plant in results:
                print(f"ID: {plant['id']}, Common Name: {plant.get('common_name', 'N/A')}, Scientific Name: {plant['scientific_name']}")
            self.view_plant_details()
        else:
            print("No plants found.")

    def view_plants_by_family(self):
        family_name = input("Enter family name: ")
        results = self.api_service.explore_plants_by_family(family_name)

        if results:
            for plant in results:
                print(f"ID: {plant['id']}, Common Name: {plant.get('common_name', 'N/A')}, Scientific Name: {plant['scientific_name']}")
        else:
            print("No plants found.")
        
        self.main_menu()

    def search_plants_by_region(self):
        region_name = input("Enter region name: ")
        results = self.api_service.search_plants_by_region(region_name)

        if results:
            for plant in results:
                print(f"ID: {plant['id']}, Common Name: {plant.get('common_name', 'N/A')}, Scientific Name: {plant['scientific_name']}")
        else:
            print("No plants found.")
        
        self.main_menu()

    def view_plant_details(self):
        plant_id = input("Enter the plant ID for details: ")
        plant_details = self.api_service.get_plant_details(plant_id)

        if plant_details:
            # Print the entire response to inspect the structure and debug
            print("Raw API Response for Plant Details:")
            print(plant_details)

            # Safely extract fields using .get() to avoid KeyErrors
            print(f"Common Name: {plant_details.get('common_name', 'N/A')}")
            print(f"Scientific Name: {plant_details.get('scientific_name', 'N/A')}")
            print(f"Family: {plant_details.get('family', {}).get('name', 'N/A')}")
            print(f"Genus: {plant_details.get('genus', {}).get('name', 'N/A')}")

            # Handle species field as a list
            species_list = plant_details.get('species', [])
            if species_list:
                print("Species Information:")
                for species in species_list:
                    print(f"  - Species Name: {species.get('scientific_name', 'N/A')}")
            else:
                print("Species: N/A")

            print(f"Growth Habit: {plant_details.get('growth_habit', 'N/A')}")
            print(f"Bloom Period: {plant_details.get('bloom_period', 'N/A')}")
            print(f"Conservation Status: {plant_details.get('conservation_status', 'N/A')}")
            print(f"Image URL: {plant_details.get('image_url', 'N/A')}")
        else:
            print("No details found for this plant.")
        
        self.main_menu()
