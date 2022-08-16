from bs4 import BeautifulSoup
import requests

class WikipediaSearch():
    def __init__(self, query, lang='en'):
        self.query = query
        self.lang = lang
        self.url = f"https://{self.lang}.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
        self.r = requests.get(self.url)
        self.content = self.r.json()

    def get_results(self):
        return self.content