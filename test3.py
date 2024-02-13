import requests

API_KEY = '445678943335678900979979-8756'

def make_api_request(endpoint, params=None):
    try:
        response = requests.get(endpoint, params=params, headers={'Authorization': f'Bearer {API_KEY}'})
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

try:
    api_endpoint = 'https://api.example.com/data'
    api_params = {'param1': 'value1', 'param2': 'value2'}
    result = make_api_request(api_endpoint, params=api_params)

    if result:
        print("API Response:", result)
    else:
        print("Failed to fetch data from API.")
except IndexError as index_err:
    print(f"Index error occurred: {index_err}")
except KeyError as key_err:
    print(f"Key error occurred: {key_err}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
