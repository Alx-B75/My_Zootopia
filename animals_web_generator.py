import json
import os

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
animals_data = load_data('animals_data.json')

for animal in animals_data:
    animal_name = animal.get('name', 'Unknown')
    animal_diet = animal.get('characteristics', {}).get('diet', 'Unknown')
    animal_location = animal.get('locations', ['Unknown'])[0]
    animal_type = animal.get('characteristics', {}).get('type', 'Unknown')
    print(f"Name: {animal_name}") 
    print(f"Diet: {animal_diet}") 
    print(f"Location: {animal_location}") 
    if animal_type == 'Unknown':
        print()
    else: 
        print(f"Type: {animal_type}")
    print()

