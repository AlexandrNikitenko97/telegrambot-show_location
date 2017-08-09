# get google maps coordinates

import urllib.parse   # for encode url
import requests


def get_json_data(address):
    main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
    url = main_api + urllib.parse.urlencode({'address': address})
    json_data = requests.get(url).json()
    return json_data


def get_formatted_address(address):
    json_data = get_json_data(address)
    try:
        formatted_address = json_data['results'][0]['formatted_address']
    except Exception:
        return None
    else:
        return str(formatted_address)


def get_coordinates(address):
    json_data = get_json_data(address)
    try:
        coordinates = json_data['results'][0]['geometry']['location']
    except Exception:
        return None
    else:
        return coordinates
