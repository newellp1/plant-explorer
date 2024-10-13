from PlantExplorer import PlantExplorer
from TrefleAPIService import TrefleAPIService

if __name__ == "__main__":
    # Create an instance of the TrefleAPIService
    api_service = TrefleAPIService()

    # Create an instance of the PlantExplorer class, passing the api_service
    explorer = PlantExplorer(api_service)

    # Run the main menu
    explorer.main_menu()
