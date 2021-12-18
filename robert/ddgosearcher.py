from .searcher import Searcher
from .constants import ENGINE_URL
from .exceptions import UnknownSafeSearchType
from bs4 import BeautifulSoup

class DuckDuckGoSearcher(Searcher):
    def __init__(self, *args):
        super().__init__(*args, engine='ddgo')
    
    def parse(self, response: str) -> []:
        result = []
        html = BeautifulSoup(response, "html.parser")
        divs = html.find_all("div", attrs={"class": "result results_links results_links_deep web-result"})
        for content in divs:
            link, title = content.find("a", href=True), content.find("h2")
            if link and title:
                result.append(link["href"])
        return result

    def search(self, data: str, safesearch: int = 1) -> []:
        if not safesearch in [1, 0, -1]:
            raise UnknownSafeSearchType(safesearch)
        url = self.url + f'?q={data}&kp={safesearch}&kl={self.language}&kc=-1'
        print(url)
        res = self.request(url)
        return self.parse(res)