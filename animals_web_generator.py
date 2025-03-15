import json
import os

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    

def load_template():
    with open('animals_template.html', 'r') as file:
        page_data = file.read()
        return page_data
  

def get_animal_data(animal_data):
    output = ''
    for animal in animal_data:
        animal_name = animal.get('name', 'Unknown')
        animal_diet = animal.get('characteristics', {}).get('diet', 'Unknown')
        animal_location = animal.get('locations', ['Unknown'])[0]
        animal_type = animal.get('characteristics', {}).get('type', 'Unknown')
        
        output += f"""
        <li class="cards__item">
            <div class="card__title"><strong>Name: {animal_name}</strong></div>
            <div class="card__text"><strong>Diet:</strong> {animal_diet}</div>
            <div class="card__text"><strong>Location:</strong> {animal_location}</div>
            <div class="card__text"><strong>Type:</strong> {animal_type}</div>
        </li>"""
    return output


def replace_data(animals_data, page_template):
    new_data = get_animal_data(animals_data)
    page_template = page_template.replace('__REPLACE_ANIMALS_INFO__', new_data)
    return page_template 


def main():
    animals_data = load_data('animals_data.json')
    page_template = load_template()
    updated_page = replace_data(animals_data, page_template)
    with open('animals.html', 'w') as file:
        file.write(updated_page)

if __name__ == '__main__':
    main()
