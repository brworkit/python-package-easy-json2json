
from easyjson2json.json2json import Json2Json

def translate(template, source):           
    translator = Json2Json(template=template, source=source)
    print(f"translate result: {translator.get_result()}")
    return translator.get_result()

def test_translate_one_level():    
    source = { "name": "Test Name" }    
    template = { "name": "name" }
    result = translate(template, source)
    assert result["name"] == source["name"]
