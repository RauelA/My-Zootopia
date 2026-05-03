import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_all_animals():
    """ Prints all animals """
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        print(f"\nName: {animal["name"]}")
        print(f"Diet: {animal["characteristics"]["diet"]}")
        print(f"Location: {animal["locations"][0]}")
        print(f"Type: {animal["characteristics"]["type"]}")

print_all_animals()