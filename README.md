# Easy JSON2JSON
    
## Description
A python package for deep JSON translation.

You just need to specify you template to get all data from another JSON to avoid doing that manually in your code.

# Install 
    pip install easy-json2json

# Usage example 

## Case #1 Simple JSON
```python

from easyjson2json import Json2Json

source = {"name": "Test Name"} # source JSON

template = {"first_name": "name"} # this is the structure you want your new JSON be 

translator = Json2Json(template=template, source=source)

result = translator.get_result()       

print(result)

# {'first_name': 'Test Name'}

```

## Case #2 Different structure
```python

from easyjson2json import Json2Json

source = {"name": "Test Name", "address": {"name": "My Street", "number": 23}} # when is not a plain JSON

template = {"first_name": "name", "address_name": ["address", "name"]} # you don't want all that structure 

translator = Json2Json(template=template, source=source)

result = translator.get_result()       

print(result)

# {'first_name': 'Test Name', 'address_name': 'My Street'}

```

## Case #3 From ugly JSON
```python

from easyjson2json import Json2Json

source = {"name": "My Name", "ADDRESS": {"name": "My Street", "number": 23}} # ugly JSON happens 

template = {"name": "name", "address": {"_source": "ADDRESS", "name": "name", "number": "number"}} # you want beautiful JSON

translator = Json2Json(template=template, source=source)

result = translator.get_result()       

print(result)

# {'name': 'My Name', 'address': {'name': 'My Street', 'number': 23}}
```

## Case #4 From List in JSON
```python

from easyjson2json import Json2Json

source = {"name": "My Name", "ADDRESSES": [{"name": "My Street", "number": 23}]} # when you have a list

template = {"name": "name", "addresses": {"_source_": "ADDRESSES", "name": "name", "number": "number"}} # then you get that list beautifuly

translator = Json2Json(template=template, source=source)

result = translator.get_result()       

print(result)

# {'name': 'My Name', 'addresses': [{'name': 'My Street', 'number': 23}]}

```


## Source Code

[easyjson2json](https://github.com/brworkit/python-package-easy-json2json.git)

## Author

[**2020 brworkit**](https://github.com/brworkit).