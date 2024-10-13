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
                self.search_plants()  # Call to search plants by name
            elif choice == "2":
                self.view_plants_by_family()  # Call to view plants by family
            elif choice == "3":
                self.search_plants_by_region()  # Call to search plants by region
            elif choice == "4":
                print("Exiting Plant Explorer...")
                break  # Exit the loop
            else:
                print("Invalid choice. Please try again.")

    # Method to search plants by name
    def search_plants(self):
        plant_name = input("Enter plant name: ")
        results = self.api_service.search_plants_by_name(plant_name)

        if results:
            for plant in results:
                print(f"ID: {plant['id']}, Common Name: {plant.get('common_name', 'N/A')}, Scientific Name: {plant['scientific_name']}")
        else:
            print("No plants found.")

    # Method to view plants by family
    def view_plants_by_family(self):
        family_name = input("Enter family name: ")
        results = self.api_service.explore_plants_by_family(family_name)

        if results:
            for plant in results:
                print(f"ID: {plant['id']}, Common Name: {plant.get('common_name', 'N/A')}, Scientific Name: {plant['scientific_name']}")
        else:
            print("No plants found.")

    # Method to search plants by region
    def search_plants_by_region(self):
        region_name = input("Enter region name: ")
        results = self.api_service.search_plants_by_region(region_name)

        if results:
            for plant in results:
                print(f"ID: {plant['id']}, Common Name: {plant.get('common_name', 'N/A')}, Scientific Name: {plant['scientific_name']}")
        else:
            print("No plants found.")
