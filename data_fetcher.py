import requests

API_KEY = "3BWyYfqgKXRHZBts21pxS9F7SkIpEyV9WMXMNh90"
url = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name' and returns a list of animals as a dictionary
    """

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    return data