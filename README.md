# Easy JSON Validator
    
## Description
A python package for deep json translation.

# Install 
    pip install easy-json2json

# Usage example 

## Case #1
```python

from easyjson2json import Json2Json

source = {"name": "Test Name"} # your json

template = {"first_name": "name"} # this is the structure you want your new json be 

translator = Json2Json(template=template, source=source)

result = translator.get_result()       

print(result)

# {'first_name': 'Test Name'}

```

## Source Code

[easyjson2json](https://github.com/brworkit/python-package-easy-json2json.git)

## Author

[**2020 brworkit**](https://github.com/brworkit).