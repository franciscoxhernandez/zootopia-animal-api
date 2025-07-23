import requests

def main():
    """Proof of concept, connection for APY-Ninjas"""
    name = input("I need information about (enter animal name): ")
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': 'gbhG5zXlusHL4o5dgJ7RxQ==OYecyDBtpCoL1PCG'})
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
        print(f"Type: {animal['taxonomy']['class']}")
        print(f"Scientific name: {animal['taxonomy']['scientific_name']}")
        print(f"Diet: {animal['characteristics']['diet']}")
        print(f"Weight: {animal['characteristics']['weight']}")
        print("-"*50)


if __name__ == '__main__':
    main()