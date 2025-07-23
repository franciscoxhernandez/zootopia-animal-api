import requests

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def main():
    """Proof of concept, connection for APY-Ninjas"""
    name = input("I need information about (enter animal name): ")
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': f"{API_KEY}"})
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    animals_data = response.json()

    if not animals_data:
        print("No animals found")
        return
    for animal in animals_data:
        print("-" * 50)
        print(f"{animal['name']}")
        print(f"Location: {animal['locations']}")
        print("-"*50)


if __name__ == '__main__':
    main()