from requests import get, exceptions
from .exceptions import *
from .constants import *

class Searcher:
    def __init__(self, language: str, engine: str):
        self.engine = engine
        self.url = ENGINE_URL[self.engine]
        if not self.check_language(language.lower()):
            raise LanguageNotSupported()
        else:
            self.language = language.lower()
        self.user_agent = USER_AGENT
    
    def check_language(self, language: str) -> bool:
        """
        Checks if a language is supported.

        @param language: Language to check
        @return: True if is a supported language, false if not
        @rtype: bool
        """
        for lang in LANGUAGUES[self.engine]:
            if language in lang:
                return True
        return False

    def request(self, url: str) -> str:
        """
        Makes a GET request to a specific URL

        @param url: URL to request
        @return: Response text
        @rtype: str
        """

        res = get(url, headers = self.user_agent)
        try:
            res.raise_for_status()
        except exceptions.HTTPError as e:
            print('An error occurred:', e)
        return res.text

    def parse(self, text: str) -> []:
        """
        Parses a HTML text to get urls from hrefs

        @param text: HTML to parse
        @type text: str
        @return: Parsed urls
        @rtype: list
        """
        pass

    def search(self, data: str, limit: int = 10) -> []:
        """
        Search a term on the search engine

        @param data: Term to search
        @type data: str
        @param limit: Limit to search
        @type limit: int
        @return: Search result
        @rtype: list
        """
        pass