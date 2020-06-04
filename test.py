import json


def read(field, source):
    return source[field] if field in source else None


def read_cnaes(source):
    # TODO: read main cnae
    def format_cnae(value):
        result = value.split(" - ")
        return result[0], result[1]

    result = [{"code": source["Cnae"],
               "description": source["MainEconomicActivity"]}]

    for index in range(0, 1000):
        value = read(f"SecondaryActivity.{index}", source)
        if value is None:
            break
        code, description = format_cnae(value)
        cnae = {"code": code, "description": description}
        result.append(cnae)

    return result


def read_phones(source):

    def format_phone(value):
        return value[:2], value[2:]

    result = []
    for index in range(0, 1000):
        value = read(f"Phone.{index}", source)
        if value is None:
            break
        area, number = format_phone(value)
        cnae = {"area": area, "number": number}
        result.append(cnae)

    return result


def read_addresses(source):
    result = []
    for index in range(0, 1000):
        value = read(f"Address.Core.{index}", source)
        if value is None:
            break
        item = {
            "city": read(f"Address.City.{index}", additional_data),
            "complement": read(f"Address.Complement.{index}", additional_data),
            "country": "BRASIL",
            "municipality": None,
            "neighborhood": read(f"Address.Neighborhood.{index}", additional_data),
            "number": read(f"Address.Number.{index}", additional_data),
            "state": read(f"Address.State.{index}", additional_data),
            "street": read(f"Address.Core.{index}", additional_data),
            "zip": read(f"Address.ZipCode.{index}", additional_data)
        }
        result.append(item)

    return result


source = {
    "Origin": "Receita-Federal Status",
    "InputParameters": "doc{08744817000186}",
    "ProtocolNumber": "",
    "BaseStatus": "ATIVA",
    "AdditionalOutputData": {
        "OfficialName": "DOCK SOLUCOES EM MEIOS DE PAGAMENTO S A",
        "BusinessName": "",
        "FoundingDate": "29/03/2007",
        "FederalEntity": "",
        "CompanyType": "MATRIZ",
        "Cnae": "63.11-9-00",
        "MainEconomicActivity": "Tratamento de dados, provedores de serviços de aplicação e serviços de hospedagem na internet (Dispensada *)",
        "LegalNatureCode": "205-4",
        "LegalNature": "Sociedade Anônima Fechada",
        "StatusDate": "29/03/2007",
        "QueryTime": "09:11:40",
        "TerminationDate": "",
        "SpecialSituation": "",
        "SpecialSituationDate": "",
        "StatusReason": "",
        "SecondaryActivity.0": "62.02-3-00 - Desenvolvimento e licenciamento de programas de computador customizáveis",
        "SecondaryActivity.1": "62.04-0-00 - Consultoria em tecnologia da informação",
        "SecondaryActivity.2": "62.09-1-00 - Suporte técnico, manutenção e outros serviços em tecnologia da informação",
        "SecondaryActivity.3": "64.63-8-00 - Outras sociedades de participação, exceto holdings",
        "SecondaryActivity.4": "64.99-9-99 - Outras atividades de serviços financeiros não especificadas anteriormente",
        "SecondaryActivity.5": "66.12-6-05 - Agentes de investimentos em aplicações financeiras",
        "SecondaryActivity.6": "66.13-4-00 - Administração de cartões de crédito",
        "SecondaryActivity.7": "66.30-4-00 - Atividades de administração de fundos por contrato ou comissão",
        "SecondaryActivity.8": "70.20-4-00 - Atividades de consultoria em gestão empresarial, exceto consultoria técnica específica",
        "SecondaryActivity.9": "74.90-1-04 - Atividades de intermediação e agenciamento de serviços e negócios em geral, exceto imobiliários",
        "SecondaryActivity.10": "82.91-1-00 - Atividades de cobranças e informações cadastrais",
        "SecondaryActivity.11": "82.99-7-99 - Outras atividades de serviços prestados principalmente às empresas não especificadas anteriormente",
        "Phone.0": "1138891800",
        "Address.Core.0": "AV TAMBORE",
        "Address.City.0": "BARUERI",
        "Address.Complement.0": "CONJ  101B",
        "Address.Neighborhood.0": "TAMBORE",
        "Address.Number.0": "267",
        "Address.State.0": "SP",
        "Address.ZipCode.0": "06.460-000",
        "Email.0": "NUMBERS@DOCK.TECH"
    },
    "QueryDate": "2020-06-04T00:00:00"
}

expected = {
    "legalStatus": "ATIVA",
    "nationalRegistration": "doc{08744817000186}",
    "establishmentDate": "29/03/2007",
    "legalName": "DOCK SOLUCOES EM MEIOS DE PAGAMENTO S A",
    "revenue": None,
    "tradeName": None,
    "categorySize": None,
    "employees": None,
    "legalNature": {
        "code": "205-4",
        "description": "Sociedade An\u00f4nima Fechada"
    },
    "legalRepresentation": {
        "name": None,
        "nationalRegistration": None
    },
    "addresses": [
        {
            "city": "BARUERI",
            "complement": "CONJ  101B",
            "country": "BRASIL",
            "municipality": None,
            "neighborhood": "TAMBORE",
            "number": "267",
            "state": "SP",
            "street": "AV TAMBORE",
            "zip": "06.460-000"
        }
    ],
    "cnaes": [
        {
            "code": "63.11-9-00",
            "description": "Tratamento de dados, provedores de serviços de aplicação e serviços de hospedagem na internet (Dispensada *)"
        },
        {
            "code": "62.02-3-00",
            "description": "Desenvolvimento e licenciamento de programas de computador customizáveis"
        },
        {
            "code": "62.04-0-00",
            "description": "Consultoria em tecnologia da informação"
        },
        {
            "code": "62.09-1-00",
            "description": "Suporte técnico, manutenção e outros serviços em tecnologia da informação"
        },
        {
            "code": "64.63-8-00",
            "description": "Outras sociedades de participação, exceto holdings"
        },
        {
            "code": "64.99-9-99",
            "description": "Outras atividades de serviços financeiros não especificadas anteriormente"
        },
        {
            "code": "66.12-6-05",
            "description": "Agentes de investimentos em aplicações financeiras"
        },
        {
            "code": "66.13-4-00",
            "description": "Administração de cartões de crédito"
        },
        {
            "code": "66.30-4-00",
            "description": "Atividades de administração de fundos por contrato ou comissão"
        },
        {
            "code": "70.20-4-00",
            "description": "Atividades de consultoria em gestão empresarial, exceto consultoria técnica específica"
        },
        {
            "code": "74.90-1-04",
            "description": "Atividades de intermediação e agenciamento de serviços e negócios em geral, exceto imobiliários"
        },
        {
            "code": "82.91-1-00",
            "description": "Atividades de cobranças e informações cadastrais"
        },
        {
            "code": "82.99-7-99",
            "description": "Outras atividades de serviços prestados principalmente às empresas não especificadas anteriormente"
        }
    ],
    "phones": [
        {
            "area": "11",
            "number": "38891800"
        }
    ],
    "partners": []
}


root = source
additional_data = source["AdditionalOutputData"]

result = {
    "legalStatus": read("BaseStatus", root),
    "nationalRegistration": read("InputParameters", root),
    "establishmentDate": read("FoundingDate", additional_data),
    "legalName": read("OfficialName", additional_data),
    "revenue": None,
    "tradeName": None,
    "categorySize": None,
    "employees": None,
    "legalNature": {
        "code": read("LegalNatureCode", additional_data),
        "description": read("LegalNature", additional_data)
    },
    "legalRepresentation": {
        "name": None,
        "nationalRegistration": None
    },
    "addresses": read_addresses(additional_data),
    "cnaes": read_cnaes(additional_data),
    "phones": read_phones(additional_data),
    "partners": []
}


print(json.dumps(result, indent=2))

print(result == expected)
