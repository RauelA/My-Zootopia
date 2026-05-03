import json


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


def __main__():
    generate_html()


if __name__ == "__main__":
    __main__()