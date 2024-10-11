from TrefleAPIService import TrefleAPIService

class PlantExplorer:
    def __init__(self):
        self.api_service = TrefleAPIService()

    def main_menu(self):
        while True:
            print("\n--- Plant Explorer ---")
            print("1. Search Plants by Name")
            print("2. View Plants by Family")
            print("3. Search Plants by Region")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.search_plants()
            elif choice == '2':
                self.view_families()
            elif choice == '3':
                self.search_region()
            elif choice == '4':
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please try again.")

    def search_plants(self):
        name = input("Enter plant name: ")
        plants = self.api_service.search_plants(name)
        if plants:
            for plant in plants['data']:
                print(f"ID: {plant['id']}, Common Name: {plant['common_name']}, Scientific Name: {plant['scientific_name']}")
            self.view_plant_details()
        else:
            print("No plants found for the given name.")

    def view_families(self):
        family = input("Enter family name: ")
        plants = self.api_service.search_by_family(family)
        if plants:
            for plant in plants['data']:
                print(f"ID: {plant['id']}, Common Name: {plant['common_name']}, Scientific Name: {plant['scientific_name']}")
        else:
            print("No plants found for the given family.")

    def search_region(self):
        region = input("Enter region name: ")
        plants = self.api_service.search_by_region(region)
        if plants:
            for plant in plants['data']:
                print(f"ID: {plant['id']}, Common Name: {plant['common_name']}, Scientific Name: {plant['scientific_name']}")
        else:
            print("No plants found for the given region.")

    def view_plant_details(self):
        plant_id = input("Enter the plant ID for details: ")
        plant_details = self.api_service.get_plant_detail(plant_id)
        if plant_details:
            print(f"Common Name: {plant_details['common_name']}")
            print(f"Scientific Name: {plant_details['scientific_name']}")
            print(f"Family: {plant_details['family']['name']}")
            print(f"Genus: {plant_details['genus']['name']}")
            print(f"Growth Habit: {plant_details.get('growth_habit', 'Unknown')}")
            print(f"Bloom Period: {plant_details.get('bloom_period', 'Unknown')}")
        else:
            print("No details available for the given plant ID.")
