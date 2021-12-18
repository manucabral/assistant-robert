from robert import GoogleSearch, DuckDuckGoSearcher

ddgo_client = DuckDuckGoSearcher('ar-es')
result = ddgo_client.search('hola', safesearch=-1)
print(result)