
    ***                        ***
    ***  ANIMAL WEB GENERATOR  ***
    ***                        ***

    This project generates a simple HTML website displaying information about animals.
    The data can either come from a local JSON file or be fetched dynamically from an external API.
    This project demonstrates:
    - API integration using requests
    - Environment variable handling with python-dotenv
    - Separation of concerns (data fetching vs. presentation)
    - Basic HTML templating


    ***  Project Description  ***

    The Animal Web Generator allows users to search for animals and automatically generates a styled HTML page
    with several informations such as:
    - Scientific name
    - Family
    - Location
    - Diet
    - Lifespan


    ***  Installation  ***

    Clone the repository:
    - git clone <your-repo-url>
    - cd <your-project-folder>

    Install dependencies:
    - pip install -r requirements.txt

    Create an .env file in the root directory: API_KEY="your_personal_api_key"


    ***  Usage  ***

    - Run the program with python animals_web_generator.py
    - Enter the name of an animal (e.g. Fox, Monkey)
    - The program will fetch data from the API => A file called animals.html will be generated
    - Open animals.html in your browser to view the result.


    ***  Project Structure  ***

    project/
    │
    ├── animals_web_generator.py   # HTML generation logic
    ├── animals_template.html      # HTML template
    ├── animals_data.json          # local data source (obsolete)
    ├── data_fetcher.py            # API communication
    ├── requirements.txt           # dependencies
    ├── .env                       # API key (not committed)
    └── .gitignore


    ***  API  ***

    This project uses the API Ninjas Animals API (https://api.api-ninjas.com/v1/animals).
    Authentication via personal API Key (need to be stored in .env)


    ***  Notes  ***

    The file animals_data.json is obsolete and only kept for reference.
    Make sure your .env file is not committed to GitHub.
    If no animal is found, the generated HTML will display an error message.