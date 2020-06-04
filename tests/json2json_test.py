
from easyjson2json.json2json import Json2Json


def translate(template, source):
    translator = Json2Json(template=template, source=source)
    print(f"RESULT: {translator.get_result()}")
    return translator.get_result()

# def test_translate_one_level_one_field_ok():
#     source = {"name": "Test Name"}
#     template = {"name": "name"}
#     result = translate(template, source)
#     assert result["name"] == source["name"]


# def test_translate_one_level_source_missing_field_ok():
#     source = {"name": "Test Name"}
#     template = {"age": "age"}
#     result = translate(template, source)
#     assert result["age"] is None


# def test_translate_one_level_one_field_with_source_specified_ok():
#     source = {"NAME": "Test Name"}
#     template = {"name": {"_source": "NAME"}}
#     result = translate(template, source)
#     assert result["name"] == source["NAME"]


# def test_translate_one_level_one_field_missing_ok():
#     source = {}
#     template = {"name": "name"}
#     result = translate(template, source)
#     assert result["name"] is None


# def test_translate_one_level_one_field_missing_template():
#     source = {"name": "name"}
#     template = {}
#     result = translate(template, source)
#     assert result == {}


# def test_translate_second_level_one_field_ok():
#     source = {"name": "My Name", "address": {"number": 23}}
#     template = {"name": "name", "address": {"number": "number"}}
#     result = translate(template, source)
#     assert result["address"]["number"] == source["address"]["number"]


# def test_translate_second_level_one_field_different_source_property_name_ok():
#     source = {"name": "My Name", "ADDRESS": {"number": 23}}
#     template = {"name": "name", "address": {
#         "_source": "ADDRESS", "number": "number"}}
#     result = translate(template, source)
#     assert result["address"]["number"] == source["ADDRESS"]["number"]


# def test_translate_second_level_one_field_different_source_property_name_deep_ok():
#     source = {"name": "My Name", "ADDRESS": {"NUMBER": 23}}
#     template = {"name": "name", "address": {
#         "_source": "ADDRESS", "number": {"_source": "NUMBER"}}}
#     result = translate(template, source)
#     assert result["address"]["number"] == source["ADDRESS"]["NUMBER"]


# def test_translate_array_one_level_ok():
#     source = {"name": "My Name", "addresses": [{"number": 23}]}
#     template = {"name": "name", "addresses": {"number": "number"}}
#     result = translate(template, source)
#     assert result["addresses"][0]["number"] == source["addresses"][0]["number"]


# def test_translate_array_one_level_different_source_property_name_ok():
#     source = {"name": "My Name", "addresses": [{"NUMBER": 23}]}
#     template = {"name": "name", "addresses": {"number": {"_source": "NUMBER"}}}
#     result = translate(template, source)
#     assert result["addresses"][0]["number"] == source["addresses"][0]["NUMBER"]


# def test_translate_array_second_level_ok():
#     source = {"name": "My Name", "addresses": [
#         {"complement": {"type": "HOUSE"}}]}
#     template = {"name": "name", "addresses": {"complement": {"type": "type"}}}
#     result = translate(template, source)
#     assert result["addresses"][0]["complement"]["type"] == source["addresses"][0]["complement"]["type"]


# def test_translate_array_second_level_different_source_property_name_ok():
#     source = {"name": "My Name", "addresses": [
#         {"complement": {"TYPE": "HOUSE"}}]}
#     template = {"name": "name", "addresses": {
#         "complement": {"type": {"_source": "TYPE"}}}}
#     result = translate(template, source)
#     assert result["addresses"][0]["complement"]["type"] == source["addresses"][0]["complement"]["TYPE"]


# def test_translate_one_level_multiple_fields_ok():
#     source = {"name": "Test Name", "birth": "2020-06-03"}
#     template = {"name": "name", "birth": "birth"}
#     result = translate(template, source)
#     assert result == source


# def test_translate_second_level_multiple_fields_in_deep_ok():
#     source = {"game": {"name": "Test Name", "details": {"type": "2D GAME"}}, "category": {
#         "name": "Category Name", "factory": {"name": "Brworkit Games"}}}
#     template = {"game": {"name": "name", "details": {"type": "type"}},
#                 "category": {"name": "name", "factory": {"name": "name"}}}
#     result = translate(template, source)
#     assert result == source


# def test_translate_second_level_multiple_fields_in_deep_different_source_property_name_ok():
#     source = {"GAME": {"nAmE": "Test Name", "DETAILS": {"TYPE": "2D GAME"}}, "CATEGORY": {
#         "nAmE": "Category Name", "FACTORY": {"nAmE": "Brworkit Games"}}}
#     template = {"game": {"_source": "GAME", "name": {"_source": "nAmE"}, "details": {"_source": "DETAILS", "type": {"_source": "TYPE"}}},
#                 "category": {"_source": "CATEGORY", "name": {"_source": "nAmE"}, "factory": {"_source": "FACTORY", "name": {"_source": "nAmE"}}}}
#     result = translate(template, source)
#     assert result["game"]["name"] == source["GAME"]["nAmE"]
#     assert result["game"]["details"]["type"] == source["GAME"]["DETAILS"]["TYPE"]
#     assert result["category"]["name"] == source["CATEGORY"]["nAmE"]
#     assert result["category"]["factory"]["name"] == source["CATEGORY"]["FACTORY"]["nAmE"]


# def test_translate_fucking_deep_level_ok():
#     source = {"kingdom": {"phylum": {
#         "class": {"order": {"family": {"genus": {"species": ["MAMALS"]}}}}}}}
#     template = {"species": ["kingdom", "phylum",
#                             "class", "order", "family", "genus", "species"]}
#     result = translate(template, source)
#     assert result["species"] == ["MAMALS"]


# def test_translate_complex_case_ok():
#     source = {
#         "result": [
#             {
#                 "certificates": [
#                     {
#                         "origin": "RECITA FEDERAL"
#                     }
#                 ]
#             }
#         ]
#     }

#     template = {"source": ["result", "certificates", "origin"]}

#     result = translate(template, source)

#     assert result["source"] == "RECITA FEDERAL"


def test_complex():
    source = {"Origin":"Receita-Federal Status","InputParameters":"doc{08744817000186}","ProtocolNumber":"","BaseStatus":"ATIVA","AdditionalOutputData":{"OfficialName":"DOCK SOLUCOES EM MEIOS DE PAGAMENTO S A","BusinessName":"","FoundingDate":"29/03/2007","FederalEntity":"","CompanyType":"MATRIZ","Cnae":"63.11-9-00","MainEconomicActivity":"Tratamento de dados, provedores de serviços de aplicação e serviços de hospedagem na internet (Dispensada *)","LegalNatureCode":"205-4","LegalNature":"Sociedade Anônima Fechada","StatusDate":"29/03/2007","QueryTime":"09:11:40","TerminationDate":"","SpecialSituation":"","SpecialSituationDate":"","StatusReason":"","SecondaryActivity.0":"62.02-3-00 - Desenvolvimento e licenciamento de programas de computador customizáveis","SecondaryActivity.1":"62.04-0-00 - Consultoria em tecnologia da informação","SecondaryActivity.2":"62.09-1-00 - Suporte técnico, manutenção e outros serviços em tecnologia da informação","SecondaryActivity.3":"64.63-8-00 - Outras sociedades de participação, exceto holdings","SecondaryActivity.4":"64.99-9-99 - Outras atividades de serviços financeiros não especificadas anteriormente","SecondaryActivity.5":"66.12-6-05 - Agentes de investimentos em aplicações financeiras","SecondaryActivity.6":"66.13-4-00 - Administração de cartões de crédito","SecondaryActivity.7":"66.30-4-00 - Atividades de administração de fundos por contrato ou comissão","SecondaryActivity.8":"70.20-4-00 - Atividades de consultoria em gestão empresarial, exceto consultoria técnica específica","SecondaryActivity.9":"74.90-1-04 - Atividades de intermediação e agenciamento de serviços e negócios em geral, exceto imobiliários","SecondaryActivity.10":"82.91-1-00 - Atividades de cobranças e informações cadastrais","SecondaryActivity.11":"82.99-7-99 - Outras atividades de serviços prestados principalmente às empresas não especificadas anteriormente","Phone.0":"1138891800","Address.Core.0":"AV TAMBORE","Address.City.0":"BARUERI","Address.Complement.0":"CONJ  101B","Address.Neighborhood.0":"TAMBORE","Address.Number.0":"267","Address.State.0":"SP","Address.ZipCode.0":"06.460-000","Email.0":"NUMBERS@DOCK.TECH"},"QueryDate":"2020-06-04T00:00:00"}
    
    # template =  {
    #         "legalStatus": "BaseStatus",
    #         "nationalRegistration": "InputParameters",
    #         "establishmentDate": ["AdditionalOutputData", "FoundingDate"],
    #         "legalName": ["AdditionalOutputData", "OfficialName"],
    #         "revenue": None,
    #         "tradeName": None,
    #         "categorySize": None,
    #         "employees": None,
    #         "legalNature": {
    #             "_source": "AdditionalOutputData",
    #             "code": "LegalNatureCode",
    #             "description": "LegalNature"
    #         },
    #         "addresses": [
    #             {   
    #                 "city": ["AdditionalOutputData", "Address.City.0"],
    #                 "complement": ["AdditionalOutputData", "Address.Complement.0"],
    #                 "country": "BRASIL",
    #                 "municipality": None,
    #                 "neighborhood": ["AdditionalOutputData", "Address.Neighborhood.0"],
    #                 "number": ["AdditionalOutputData", "Address.Number.0"],
    #                 "state": ["AdditionalOutputData", "Address.State.0"],
    #                 "street": ["AdditionalOutputData", "Address.Core.0"],
    #                 "zip": ["AdditionalOutputData", "Address.ZipCode.0"]
    #             }
    #         ]                        
    #     }

    template =  {            
            "AdditionalOutputData": 
                {   
                    "city": ["AdditionalOutputData", "Address.City.0"],
                    "complement": ["AdditionalOutputData", "Address.Complement.0"],
                    "country": "BRASIL",
                    "municipality": None,
                    "neighborhood": ["AdditionalOutputData", "Address.Neighborhood.0"],
                    "number": ["AdditionalOutputData", "Address.Number.0"],
                    "state": ["AdditionalOutputData", "Address.State.0"],
                    "street": ["AdditionalOutputData", "Address.Core.0"],
                    "zip": ["AdditionalOutputData", "Address.ZipCode.0"]
                }
                                    
        }


    result = translate(template, source)

    # assert result["legalStatus"] == source["BaseStatus"]
    # assert result["nationalRegistration"] == source["InputParameters"]
    # assert result["establishmentDate"] == source["AdditionalOutputData"]["FoundingDate"]
    # assert result["legalName"] == source["AdditionalOutputData"]["OfficialName"]
    # assert result["revenue"] is None
    # assert result["tradeName"] is None
    # assert result["categorySize"] is None
    # assert result["employees"] is None
    # assert result["legalNature"]["code"] == source["AdditionalOutputData"]["LegalNatureCode"]
    # assert result["legalNature"]["description"] == source["AdditionalOutputData"]["LegalNature"]

    # assert result["addresses"][0]["city"] == source["AdditionalOutputData"]["Address.City.0"]
    assert result["AdditionalOutputData"]["city"] == source["AdditionalOutputData"]["Address.City.0"]





















# template =  {
    #         "legalStatus": "BaseStatus",
    #         "nationalRegistration": "CNPJ",
    #         "establishmentDate": "FoundingDate",
    #         "legalName": "OfficialName",
    #         "revenue": None,
    #         "tradeName": None,
    #         "categorySize": None,
    #         "employees": None
    #         ,
    #         "legalNature": {
    #             "_source": "AdditionalOutputData",
    #             "code": "LegalNatureCode",
    #             "description": "LegalNature"
    #         },
    #         "legalRepresentation": {
    #             "_source": "AdditionalOutputData",
    #             "name": None,
    #             "nationalRegistration": None
    #         },
    #         "addresses": [
    #             {
    #                 "city": "Address.City.0",
    #                 "complement": "Address.Complement.0",
    #                 "country": "BRASIL",
    #                 "municipality": None,
    #                 "neighborhood": "Address.Neighborhood.0",
    #                 "number": "Address.Number.0",
    #                 "state": "Address.State.0",
    #                 "street": "Address.Core.0",
    #                 "zip": "Address.ZipCode.0"
    #             }
    #         ],
    #         "cnaes": [
    #             {
    #                 "code": "Cnae",
    #                 "description": "MainEconomicActivity"
    #             },
    #             {
    #                 "code": "SecondaryActivity",
    #                 "description": "SecondaryActivity"
    #             }
    #         ],
    #         "phones": [
    #             {
    #                 "area": "Phone.0",
    #                 "number": "Phone.0"
    #             },
    #             {
    #                 "area": "Phone.X",
    #                 "number": "Phone.X"
    #             }
    #         ],
    #         "partners": []
    #     }