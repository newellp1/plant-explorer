from trefle_service import TrefleAPIService

def main():
    print("Welcome to the Plant Explorer!")
    
    # Create an instance of the Trefle API service
    trefle_service = TrefleAPIService()

    # Simple menu-driven interface
    while True:
        print("\nMenu:")
        print("1. Search for plants by name")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            plant_name = input("Enter the plant name: ")
            plants = trefle_service.search_plants(plant_name)
            if plants:
                for plant in plants:
                    print(f"Plant Name: {plant['common_name']}, Scientific Name: {plant['scientific_name']}")
            else:
                print("No plants found for the given name.")
        elif choice == "2":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
