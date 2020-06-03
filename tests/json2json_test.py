
from easyjson2json.json2json import Json2Json

def translate(template, source):           
    translator = Json2Json(template=template, source=source)
    print(f"translate result: {translator.get_result()}")
    return translator.get_result()

def test_translate_one_level_one_field_ok():    
    source = { "name": "Test Name" }    
    template = { "name": "name" }
    result = translate(template, source)
    assert result["name"] == source["name"]

def test_translate_one_level_one_field_with_source_specified_ok():    
    source = { "NAME": "Test Name" }    
    template = { "name": {"_source": "NAME"} }
    result = translate(template, source)
    assert result["name"] == source["NAME"]

def test_translate_one_level_one_field_missing_ok():    
    source = { }    
    template = { "name": "name" }
    result = translate(template, source)
    assert result["name"] is None

def test_translate_one_level_one_field_missing_template():    
    source = { "name": "name" }    
    template = { }
    result = translate(template, source)
    assert result == {}

def test_translate_second_level_one_field_ok():    
    source = { "name": "My Name", "address": { "number": 23 } }    
    template = { "name": "name", "address": { "number": "number" } }
    result = translate(template, source)
    assert result["address"]["number"] == source["address"]["number"]

def test_translate_second_level_one_field_differente_source_property_name_ok():    
    source = { "name": "My Name", "ADDRESS": { "number": 23 } }    
    template = { "name": "name", "address": { "_source": "ADDRESS", "number": "number" } }
    result = translate(template, source)
    assert result["address"]["number"] == source["ADDRESS"]["number"]

def test_translate_second_level_one_field_differente_source_property_name_deep_ok():    
    source = { "name": "My Name", "ADDRESS": { "NUMBER": 23 } }    
    template = { "name": "name", "address": { "_source": "ADDRESS", "number": {"_source": "NUMBER"} } }
    result = translate(template, source)
    assert result["address"]["number"] == source["ADDRESS"]["NUMBER"]

def test_translate_array_one_level_ok():    
    source = { "name": "My Name", "addresses": [{ "number": 23 }] }    
    template = { "name": "name", "addresses": { "number": "number" } }
    result = translate(template, source)
    assert result["addresses"][0]["number"] == source["addresses"][0]["number"]

# def test_translate_one_level_multiple_fields():    
#     source = { "name": "Test Name", "birth": "2020-06-03" }    
#     template = { "name": "name", "birth": "2020-06-03" }
#     result = translate(template, source)
#     assert result["name"] == source["name"]