from .searcher import Searcher
from .constants import ENGINE_URL
from bs4 import BeautifulSoup

class DuckDuckGoSearcher(Searcher):
    def __init__(self, *args):
        super().__init__(*args, engine='ddgo')
    
    def parse(self, response: str) -> []:
        result = []
        html = BeautifulSoup(response, "html.parser")
        divs = html.find_all("div", attrs={"class": "result__body links_main links_deep"})
        for content in divs:
            link, title = content.find("a", href=True), content.find("h3")
            if link and title:
                result.append(link["href"])
        return result

    def search(self, data: str, limit: int = 10, safesearch: int = 1) -> []:
        url = self.url + f'?q={data}&kp={safesearch}&kl={self.language}'
        print(url)
        res = self.request(url)
        print(res)
        return self.parse(res)