import requests

API_KEY = 'gbhG5zXlusHL4o5dgJ7RxQ==OYecyDBtpCoL1PCG'

def get_animal_data(animal_name):
    """This function gets animal data from API Ninjas"""
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': f"{API_KEY}"})

    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return []

    return response.json()