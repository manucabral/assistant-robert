# Assistant Robert
A simple Python library that provides search with different search engines and more.

# Install
```
pip install assistant-robert
```

# Usage
```py
from robert import GoogleSearcher

client = GoogleSearcher('en')
result = client.search('hello')
print(result)
```