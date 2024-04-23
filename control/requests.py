import os
import base64
import requests
from kindwise import PlantApi


def identify_plant(img):
    """
    Identify a plant using the Plant ID API.

    Parameters:
    img (str): The path to the image file of the plant.

    Returns:
    None

    Example:
    identify_plant('path/to/image.jpg')

    This function uses the Plant ID API to identify a plant based on an image file.
    It sends a POST request to the API endpoint 'https://api.plant.id/v3/identification'
    with the image file encoded as base64 in the request body.

    The function includes the 'url' and 'common_names' details in the identification request.
    It also sets the 'Api-Key' header with the value from the 'API_KEY' environment variable.

    The function then prints whether the identified object is a plant or not.
    It also prints the suggestions for the plant's classification,
    including the name, probability, URL, and common names.

    Note: This function requires the 'requests' package to be installed.
    """
    with open(img, 'rb') as file:
        images = [base64.b64encode(file.read()).decode('ascii')]

    response = requests.post(timeout=10,
        url='https://api.plant.id/v3/identification',
        params={'details': 'url,common_names'},
        headers={'Api-Key': os.getenv('API_PLANT_KEY')},
        json={'images': images},
    )

    identification = response.json()

    print('is plant' if identification['result']['is_plant']['binary'] else 'is not plant')
    for suggestion in identification['result']['classification']['suggestions']:
        print(suggestion['name'])
        print(f'probability {suggestion["probability"]:.2%}')
        print(suggestion['details']['url'], suggestion['details']['common_names'])
        print()

def identify_plant2(img):
    """
    Identify a plant using the PlantApi.

    Parameters:
        img (str): The path to the image file of the plant.

    Returns:
        None

    Example:
        identify_plant2('path/to/image.jpg')

    This function uses the PlantApi to identify a plant based on an image file.
    It first creates an instance of the PlantApi class using the API key stored in
    the environment variable 'API_KEY'. Then, it calls the 'identify' method of the
    PlantApi instance, passing the image file path and a list of details to include
    in the identification response.

    The function then prints whether the identified object is a plant or not.
    It also prints the suggestions for the plant's classification,
    including the name, probability, URL, and common names.

    Note: This function requires the 'kindwise' package, 'dotenv' package,
    and 'requests' package to be installed.
    """
    api = PlantApi(os.getenv('API_PLANT_KEY'))
    identification = api.identify(img, details=['url', 'common_names'])
    sugestion = identification.result.classification.suggestions[0]
    plant_wiki_url = sugestion.details['url']
    plant_name = sugestion.name
    print('name ' , plant_name)
    print('url ', plant_wiki_url)
        # print(suggestion.name)
        # print(f'probability {suggestion.probability:.2%}')
        # print(suggestion.details['url'], suggestion.details['common_names'])
        # print()
    # get_wikipedia_info(plant_wiki_url)

def trefle_identification():
    r = requests.get(url='https://trefle.io/api/v1/plants?token='+os.getenv('TREFLE_API_KEY'), timeout=10)
    print(r.json())
    
def get_wikipedia_info(url):
    
    
    title = url.split("/")[-1]

    
    api_url = "https://es.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts|info",
        "titles": title,
        "inprop": "url",
        "explaintext": True,
    }
    
    response = requests.get(api_url, params=params)
    data = response.json()

    page_id = list(data["query"]["pages"].keys())[0]
    page_info = data["query"]["pages"][page_id]
    page_url = page_info["fullurl"]
    page_title = page_info["title"]
    page_extract = page_info["extract"]

    # Print or return the information
    print("Title:", page_title)
    print("URL:", page_url)
    print("Extract:", page_extract)