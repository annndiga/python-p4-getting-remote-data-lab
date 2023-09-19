import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
            return response.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error sending GET request: {e}")

    def load_json(self):
        response_body = self.get_response_body()
        try:
            return json.loads(response_body)
        except json.JSONDecodeError as e:
            raise Exception(f"Error decoding JSON response: {e}")

# Example usage
if __name__ == "__main__":
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

    try:
        requester = GetRequester(URL)
        json_data = requester.load_json()
        print(json_data)
    except Exception as e:
        print(f"An error occurred: {e}")    
        