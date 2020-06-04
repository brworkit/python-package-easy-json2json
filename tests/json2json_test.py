
from easyjson2json.json2json import Json2Json


def translate(template, source):
    translator = Json2Json(template=template, source=source)
    print(f"result: {translator.get_result()}")
    return translator.get_result()

def test_translate_one_level_one_field_ok():
    source = {"name": "Test Name"}
    template = {"name": "name"}
    result = translate(template, source)
    assert result["name"] == source["name"]

def test_translate_one_level_source_missing_field_ok():
    source = {"name": "Test Name"}
    template = {"age": "age"}
    result = translate(template, source)
    assert result["age"] is None

def test_translate_one_level_one_field_with_source_specified_ok():
    source = {"NAME": "Test Name"}
    template = {"name": {"_source": "NAME"}}
    result = translate(template, source)
    assert result["name"] == source["NAME"]

def test_translate_one_level_one_field_missing_ok():
    source = {}
    template = {"name": "name"}
    result = translate(template, source)
    assert result["name"] is None

def test_translate_one_level_one_field_missing_template():
    source = {"name": "name"}
    template = {}
    result = translate(template, source)
    assert result == {}

def test_translate_second_level_one_field_ok():
    source = {"name": "My Name", "address": {"number": 23}}
    template = {"name": "name", "address": {"number": "number"}}
    result = translate(template, source)
    assert result["address"]["number"] == source["address"]["number"]

def test_translate_second_level_one_field_different_source_property_name_ok():
    source = {"name": "My Name", "ADDRESS": {"number": 23}}
    template = {"name": "name", "address": {
        "_source": "ADDRESS", "number": "number"}}
    result = translate(template, source)
    assert result["address"]["number"] == source["ADDRESS"]["number"]

def test_translate_second_level_one_field_different_source_property_name_deep_ok():
    source = {"name": "My Name", "ADDRESS": {"NUMBER": 23}}
    template = {"name": "name", "address": {
        "_source": "ADDRESS", "number": {"_source": "NUMBER"}}}
    result = translate(template, source)
    assert result["address"]["number"] == source["ADDRESS"]["NUMBER"]

def test_translate_array_one_level_ok():
    source = {"name": "My Name", "addresses": [{"number": 23}]}
    template = {"name": "name", "addresses": {"number": "number"}}
    result = translate(template, source)
    assert result["addresses"][0]["number"] == source["addresses"][0]["number"]

def test_translate_array_one_level_different_source_property_name_ok():
    source = {"name": "My Name", "addresses": [{"NUMBER": 23}]}
    template = {"name": "name", "addresses": {"number": {"_source": "NUMBER"}}}
    result = translate(template, source)
    assert result["addresses"][0]["number"] == source["addresses"][0]["NUMBER"]

def test_translate_array_second_level_ok():
    source = {"name": "My Name", "addresses": [
        {"complement": {"type": "HOUSE"}}]}
    template = {"name": "name", "addresses": {"complement": {"type": "type"}}}
    result = translate(template, source)
    assert result["addresses"][0]["complement"]["type"] == source["addresses"][0]["complement"]["type"]

def test_translate_array_second_level_different_source_property_name_ok():
    source = {"name": "My Name", "addresses": [
        {"complement": {"TYPE": "HOUSE"}}]}
    template = {"name": "name", "addresses": {
        "complement": {"type": {"_source": "TYPE"}}}}
    result = translate(template, source)
    assert result["addresses"][0]["complement"]["type"] == source["addresses"][0]["complement"]["TYPE"]

def test_translate_one_level_multiple_fields_ok():
    source = {"name": "Test Name", "birth": "2020-06-03"}
    template = {"name": "name", "birth": "birth"}
    result = translate(template, source)
    assert result == source

def test_translate_second_level_multiple_fields_in_deep_ok():
    source = {"game": {"name": "Test Name", "details": {"type": "2D GAME"}}, "category": {
        "name": "Category Name", "factory": {"name": "Brworkit Games"}}}
    template = {"game": {"name": "name", "details": {"type": "type"}},
                "category": {"name": "name", "factory": {"name": "name"}}}
    result = translate(template, source)
    assert result == source

def test_translate_second_level_multiple_fields_in_deep_different_source_property_name_ok():
    source = {"GAME": {"nAmE": "Test Name", "DETAILS": {"TYPE": "2D GAME"}}, "CATEGORY": {
        "nAmE": "Category Name", "FACTORY": {"nAmE": "Brworkit Games"}}}
    template = {"game": {"_source": "GAME", "name": {"_source": "nAmE"}, "details": {"_source": "DETAILS", "type": {"_source": "TYPE"}}},
                "category": {"_source": "CATEGORY", "name": {"_source": "nAmE"}, "factory": {"_source": "FACTORY", "name": {"_source": "nAmE"}}}}
    result = translate(template, source)
    assert result["game"]["name"] == source["GAME"]["nAmE"]
    assert result["game"]["details"]["type"] == source["GAME"]["DETAILS"]["TYPE"]
    assert result["category"]["name"] == source["CATEGORY"]["nAmE"]
    assert result["category"]["factory"]["name"] == source["CATEGORY"]["FACTORY"]["nAmE"]

def test_translate_fucking_deep_level_ok():
    source = {"kingdom": {"phylum": {
        "class": {"order": {"family": {"genus": {"species": ["MAMALS"]}}}}}}}
    template = {"species": ["kingdom", "phylum",
                            "class", "order", "family", "genus", "species"]}
    result = translate(template, source)
    assert result["species"] == ["MAMALS"]

def test_translate_deep_levels_from_array_ok():
    source = {
        "firstLevel": [
            {
                "secondLevel": [
                    {
                        "thirdLevel": "This is the third level"
                    }
                ]
            }
        ]
    }

    template = {"source": ["firstLevel", "secondLevel", "thirdLevel"]}

    result = translate(template, source)

    assert result["source"] == "This is the third level"


def test_example_1():
    source = {"name": "Test Name"}
    template = {"first_name": "name"}
    result = translate(template, source)
    assert result["first_name"] == source["name"]

def test_example_2():
    source = {"name": "Test Name", "address": {"name": "My Street", "number": 23}} # when is not a plain json
    template = {"first_name": "name", "address_name": ["address", "name"]} # you don't want all that structure
    result = translate(template, source)
    assert result["first_name"] == source["name"]

def test_example_3():
    source = {"name": "My Name", "ADDRESS": {"name": "My Street", "number": 23}} # ugly JSON happens 
    template = {"name": "name", "address": {"_source": "ADDRESS", "name": "name", "number": "number"}} # you want beautiful JSON
    result = translate(template, source)
    assert result["address"]["name"] == source["ADDRESS"]["name"]
    assert result["address"]["number"] == source["ADDRESS"]["number"]
    
def test_example_4():
    source = {"name": "My Name", "addresses": [{"name": "My Street", "number": 23}]}
    template = {"name": "name", "addresses": {"name": "name", "number": "number"}}
    result = translate(template, source)
    assert result["addresses"][0]["name"] == source["addresses"][0]["name"]
    assert result["addresses"][0]["number"] == source["addresses"][0]["number"]