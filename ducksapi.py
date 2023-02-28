import requests

class DucksApi:

    url="https://random-d.uk/api/v2/random"

    def get_random_duck(self):
        response = requests.get(self.url)
        if(response.status_code==200):
            return response.json()['url']
        else:
            return ""