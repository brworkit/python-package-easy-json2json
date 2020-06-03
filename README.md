# Easy JSON Validator
    
## Description
A python package for deep json parse.

# Install 
    pip install easy-json-validator

# Usage example 

## Success Case
```python

from easyjson2json import JsonValidator

source = {"name": "My Name", "birth": "2000-01-01", "salary": 1000} # your json

template = {"name": ["NotNull"]} # what you want to test 

validator = JsonValidator(template=template, source=source)       

result = validator.validate()       

print(f"result: {result}")

# result: {'name': {'value': "My Name", 'rules': ['NotNull'], 'validations': {'NotNull': {'status': 'OK'}}}}

```

## Source Code

[easyjson2json](https://github.com/brworkit/python-package-easy-json2json.git)

## Author

[**2020 brworkit**](https://github.com/brworkit).