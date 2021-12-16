from .searcher import Searcher
from .constants import ENGINE_URL
from bs4 import BeautifulSoup

class GoogleSearch(Searcher):

    def __init__(self, *args):
        super().__init__(*args, engine='google')
    
    def parse(self, response: str) -> []:
        result = []
        html = BeautifulSoup(response, "html.parser")
        divs = html.find_all("div", attrs={"class": "yuRUbf"})
        for content in divs:
            link, title = content.find("a", href=True), content.find("h3")
            if link and title:
                result.append(link["href"])
        return result

    def search(self, data: str, limit: int = 10) -> []:
        url = self.url + f'?q={data}&num={limit}&hl={self.language}'
        res = self.request(url)
        return self.parse(res)