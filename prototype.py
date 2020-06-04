def query_source_field_value(path, source):
    print(f"path_array: {path}")
    print(f"source: {source}")
    result = dict(source)
    for key in list(path):        
        print(f"key: {key}")
        print(f"new source: {result}")
        if isinstance(result, dict) and key in dict(result):
            result = result[key]                        
            if key == path[-1]:
                print(f"result: {result}")
                return result
            path.remove(key)
        elif isinstance(result, list):
            print(f"result is list")
            result = result[0]            
            return query_source_field_value(path, result)
        else: 
            break
    return None

def define_searched_key(field, template):
    if "_source" in template[field]:
        searched = template[field]["_source"]
        return searched.split(".")
    return template[field].split(".")

def translate(template, source):
    result = {}
    for field in template:
        searched_key = define_searched_key(field, template)                
        result[field] = query_source_field_value(searched_key, source)
    return result

# source = {
#     "name": "My Name", 
#     "address": {
#         "street": "My Street"
#     }, 
#     "phones": {
#         "contacts": [
#             {
#                 "name": "Contact 1"
#             }
#         ] 
#     } 
# }    

# template = {
#     "name": "name", 
#     "street": "address.street",
#     "contacts": "phones.contacts.name"
# }

source = {
    "result": [
        {
            "certificates": [
                {
                    "origin": "RECITA FEDERAL",
                    "street": "Street Name"
                }
            ]
        }
    ]
}    

template = {
    "source": "result.certificates.origin",
    "address": "result.certificates.street"
}

result = translate(template, source)

print(f"result: {result}")


