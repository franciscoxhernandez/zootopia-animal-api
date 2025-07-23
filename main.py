import requests

def get_animal_data(animal_name):
    """This function gets animal data from API Ninjas"""
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': 'gbhG5zXlusHL4o5dgJ7RxQ==OYecyDBtpCoL1PCG'})

    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return []

    data = response.json()
    if not data:
        print("No animal found.")
    return data

def serialize_animals(animals_data):
    """This functions creates the html content"""
    output = ""
    for animal in animals_data:
        name_animal = animal.get("name", "N/A")
        characteristics = animal.get("characteristics", {})
        taxonomy = animal.get("taxonomy", {})

        diet = characteristics.get("diet", "N/A")
        animal_type = taxonomy.get("class", "N/A")
        skin_type = characteristics.get("skin_type", "N/A")
        locations_list = animal.get("locations", [])
        locations = ", ".join(locations_list) if locations_list else "N/A"
        weight = characteristics.get("weight", "N/A")
        length = characteristics.get("length", "N/A")

        output += '<li class="cards__item">\n'
        output += f'    <div class="card__title">{name_animal}</div>\n'
        output += '         <div class="card__text">\n'
        output += '             <ul class="card__list">\n'
        output += f'                <li class="card__list-item"><strong>Diet:</strong> {diet}</li>\n'
        output += f'                <li class="card__list-item"><strong>Location:</strong> {locations}</li>\n'
        output += f'                <li class="card__list-item"><strong>Type:</strong> {animal_type}</li>\n'
        output += f'                <li class="card__list-item"><strong>Skin Type:</strong> {skin_type}</li>\n'
        output += f'                <li class="card__list-item"><strong>Weight:</strong> {weight}</li>\n'
        output += f'                <li class="card__list-item"><strong>Length:</strong> {length}</li>\n'
        output += '             </ul>\n'
        output += '         </div>\n'
        output += '     </li>\n'
    return output

def main():
    animal_name = input("Enter the name of an animal: ")
    animals_data = get_animal_data(animal_name)

    # Read the HTML template
    with open("animals_template.html", "r", encoding="utf-8") as file:
        template = file.read()

    # Decide what to insert based on API response
    if not animals_data:
        message = f'<h2>The animal "{animal_name}" does not exist.</h2>'
        final_html = template.replace("__REPLACE_ANIMALS_INFO__", message)
    else:
        html_content = serialize_animals(animals_data)
        final_html = template.replace("__REPLACE_ANIMALS_INFO__", html_content)

    # Write the final result
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("✅ Website generated as 'animals.html'")

if __name__ == '__main__':
    main()
