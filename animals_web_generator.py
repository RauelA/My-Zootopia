import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def animals_to_string():
    animals_data = load_data("animals_data.json")
    animals_html = ""
    for animal in animals_data:
        name = animal.get("name", "Unknown")
        diet = animal.get("characteristics", {}).get("diet", "Unknown")
        animal_type = animal.get("characteristics", {}).get("type", "Unknown")
        location = animal.get("locations", ["Unknown"])[0]

        animals_html += f"""
        <li class="cards__item">
            <div class="card__title">{name}</div>
            <div class="card__text">
                Diet: {diet}<br>
                Location: {location}<br>
                Type: {animal_type}
            </div>
        </li>
        """

    return animals_html


def generate_html():
    animals_html = animals_to_string()
    with open("animals_template.html", "r") as file:
        html_template = file.read()
    final_html = html_template.replace("{animals}", animals_html)
    with open("animals.html", "w") as file:
        file.write(final_html)


generate_html()