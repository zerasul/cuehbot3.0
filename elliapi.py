import requests

class ElliApi:

    url='http://zerasul.me:5555/api/gif'

    def get_random_elli(self):
        response = requests.get(self.url)
        if(response.status_code==200):
            return response.json()['url']
        else:
            return ""