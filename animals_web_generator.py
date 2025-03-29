import json
import os

def load_data(file_path):
    """
    Load JSON data from a file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    

def load_template():
    """
    Load the HTML template from a file.

    Returns:
        str: The content of the HTML template.
    """
    with open('animals_template.html', 'r', encoding='utf-8') as file:
        return file.read()
  

def get_animal_data(animal_data):
    """
    Generate HTML list items for animal data.

    Args:
        animal_data (list): A list of dictionaries containing animal information.

    Returns:
        str: The generated HTML string for the animal data.
    """
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
    """
    Replace placeholder in the HTML template with animal data.

    Args:
        animals_data (list): A list of dictionaries containing animal information.
        page_template (str): The HTML template string.

    Returns:
        str: The updated HTML template with animal data.
    """
    new_data = get_animal_data(animals_data)
    return page_template.replace('__REPLACE_ANIMALS_INFO__', new_data)


def save_updated_page(updated_page, output_file):
    """
    Save the updated HTML page to a file.

    Args:
        updated_page (str): The updated HTML content.
        output_file (str): The path to the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(updated_page)


def generate_html():
    """
    Generate the updated HTML content by loading data and template,
    replacing placeholders, and returning the updated content.

    Returns:
        str: The updated HTML content.
    """
    animals_data = load_data('animals_data.json')
    page_template = load_template()
    return replace_data(animals_data, page_template)


def main():
    """
    Main function to generate the animals HTML page and save it to a file.
    """
    updated_page = generate_html()
    save_updated_page(updated_page, 'animals.html')


if __name__ == '__main__':
    main()
