# Animals Web Generator

This project generates an HTML page displaying a list of animals with their details such as name, diet, location, and type. The data is loaded from a JSON file and inserted into an HTML template.

## Files

- `animals_web_generator.py`: The main script that generates the HTML page.
- `animals_data.json`: The JSON file containing the animal data.
- `animals_template.html`: The HTML template file with a placeholder for the animal data.
- `animals.html`: The generated HTML file with the animal data.

## Requirements

- Python 3.x

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Place the `animals_data.json` and `animals_template.html` files in the same directory as `animals_web_generator.py`.
3. Run the script:

    ```sh
    python animals_web_generator.py
    ```

4. The script will generate an [animals.html](http://_vscodecontentref_/0) file in the same directory.

## Example

### [animals_data.json](http://_vscodecontentref_/1)

```json
[
    {
        "name": "American Foxhound",
        "characteristics": {
            "diet": "Omnivore",
            "type": "Hound"
        },
        "locations": ["North-America"]
    },
    {
        "name": "Arctic Fox",
        "characteristics": {
            "diet": "Carnivore",
            "type": "Mammal"
        },
        "locations": ["Eurasia"]
    }
]
