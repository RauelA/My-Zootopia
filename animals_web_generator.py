import json
import requests
import os
from dotenv import load_dotenv
import data_fetcher

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """ Loads data from animals_adata.json and returns a html string """
    output = f"""
            <li class="cards__item">
                <div class="card__title">{animal_obj["name"]}</div>
                <div class="card__text">
                    <strong>Diet:</strong> {animal_obj.get("characteristics", {}).get("diet", "Unknown")}<br/>
                    <strong>Location:</strong> {animal_obj.get("locations", {})[0]}<br/>
                    <strong>Type:</strong> {animal_obj.get("characteristics", {}).get("type", "Unknown")}<br/>
                </div>
            </li>
            """
    return output


def animals_to_string():
    """ Loads data from animals_adata.json and returns a html string """
    animals_data = load_data("animals_data.json")
    animals_html = ""
    for animal in animals_data:
        animals_html += serialize_animal(animal)
    return animals_html


def generate_html():
    """ Generates a HTML file based on animals_adata.json """
    animals_html = animals_to_string()
    with open("animals_template.html", "r") as file:
        html_template = file.read()
    final_html = html_template.replace("{animals}", animals_html)
    with open("animals.html", "w") as file:
        file.write(final_html)


def generate_html_with_api():
    """ Generates a HTML file based on API """
    animals_html = fetch_animals_via_api()
    with open("animals_template.html", "r") as file:
        html_template = file.read()
    final_html = html_template.replace("{animals}", animals_html)
    with open("animals.html", "w") as file:
        file.write(final_html)


def fetch_animals_via_api():
    """ Generates a HTML file based on API """

    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = "https://api.api-ninjas.com/v1/animals"

    animal_name = input("Enter animal name: ")

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(url, headers=headers, params=params)
    print("Status code:", response.status_code)
    data = response.json()

    # HTML Start
    html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Animals</title>
        </head>
        <body>
            <h1>Animal Search Results</h1>
        """

    # HTML Data
    if len(data) == 0:
        html_content += f"<h2>The animal '{animal_name}' doesn’t exist.</h2>"
    else:
        for animal in data:
            html_content += f"<h2>{animal['name']}</h2>"

            taxonomy = animal.get("taxonomy", {})
            characteristics = animal.get("characteristics", {})

            html_content += "<ul>"

            html_content += f"<li>Scientific Name: {taxonomy.get('scientific_name', 'N/A')}</li>"
            html_content += f"<li>Family: {taxonomy.get('family', 'N/A')}</li>"
            html_content += f"<li>Location: {', '.join(animal.get('locations', []))}</li>"
            html_content += f"<li>Diet: {characteristics.get('diet', 'N/A')}</li>"
            html_content += f"<li>Lifespan: {characteristics.get('lifespan', 'N/A')}</li>"

            html_content += "</ul>"
            html_content += "<hr>"

    # HTML Ending
    html_content += """
    </body>
    </html>
    """

    return html_content


def generate_html_with_data_fetcher():
    """ Generates a HTML file based on data_fetcher.py """
    animals_html = fetch_animals_with_data_fetcher()
    with open("animals_template.html", "r") as file:
        html_template = file.read()
    final_html = html_template.replace("{animals}", animals_html)
    with open("animals.html", "w") as file:
        file.write(final_html)


def fetch_animals_with_data_fetcher():
    animal_name = input("Enter a name of an animal: ")

    data = data_fetcher.fetch_data(animal_name)

    # HTML Start
    html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Animals</title>
        </head>
        <body>
            <h1>Animal Search Results</h1>
        """

    # HTML Data
    if len(data) == 0:
        html_content += f"<h2>The animal '{animal_name}' doesn’t exist.</h2>"
    else:
        for animal in data:
            html_content += f"<h2>{animal['name']}</h2>"

            taxonomy = animal.get("taxonomy", {})
            characteristics = animal.get("characteristics", {})

            html_content += "<ul>"

            html_content += f"<li>Scientific Name: {taxonomy.get('scientific_name', 'N/A')}</li>"
            html_content += f"<li>Family: {taxonomy.get('family', 'N/A')}</li>"
            html_content += f"<li>Location: {', '.join(animal.get('locations', []))}</li>"
            html_content += f"<li>Diet: {characteristics.get('diet', 'N/A')}</li>"
            html_content += f"<li>Lifespan: {characteristics.get('lifespan', 'N/A')}</li>"

            html_content += "</ul>"
            html_content += "<hr>"

    # HTML Ending
    html_content += """
        </body>
        </html>
        """

    return html_content


def __main__():
    #generate_html()  # This is a function from Zootopia 1
    generate_html_with_data_fetcher()


if __name__ == "__main__":
    __main__()