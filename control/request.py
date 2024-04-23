import base64
import requests
from kindwise import PlantApi
from dotenv import load_dotenv
import os

def identify_plant(img):
    with open(img, 'rb') as file:
        images = [base64.b64encode(file.read()).decode('ascii')]

    response = requests.post(timeout=10,
        url='https://api.plant.id/v3/identification',
        params={'details': 'url,common_names'},
        headers={'Api-Key': os.getenv('API_KEY')},
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

    api = PlantApi(os.getenv('API_KEY'))
    identification = api.identify(img, details=['url', 'common_names'])

    print('is plant' if identification.result.is_plant.binary else 'is not plant')
    for suggestion in identification.result.classification.suggestions:
        print(suggestion.name)
        print(f'probability {suggestion.probability:.2%}')
        print(suggestion.details['url'], suggestion.details['common_names'])
        print()


def configure():
    load_dotenv()