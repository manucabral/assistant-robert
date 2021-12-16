# Robert
A simple Python web searcher library with different search engines.

# Install
```
pip install roberthelper
```

# Usage
```py
from robert import GoogleSearcher

client = GoogleSearcher('en')
result = client.search('hello')
print(result)
```