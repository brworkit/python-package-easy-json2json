# def query_source_field_value(path_array, source):
#     source_copy = dict(source)
#     for key in path_array:        
#         if isinstance(source_copy, dict) and key in dict(source_copy):
#             source_copy = source_copy[key]            
#             if key == path_array[-1]:
#                 print(f"return value 1: {source_copy}")
#                 return source_copy                                
#         elif isinstance(source_copy, list):
#             values = []
#             for item in source_copy:
#                 if key in item:
#                     print(f"return value 2: {item[field]}")
#                     return item[field]            
#         else: 
#             break
#     return None


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
        # print(f"searched_key: {searched_key}")
        result[field] = query_source_field_value(searched_key, source)

        # if exists_searched_key(searched_key, source):
        #     searched_key_data_type = get_searched_key_data_type(searched_key, source)
            
        #     if searched_key_data_type == list:
        #         pass
        #     else:
        #         result[field] = query_source_field_value(searched_key, source)                    
        # else:
        #     result[field] = None                        
        
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
                    "origin": "RECITA FEDERAL"
                }
            ]
        }
    ]
}    

template = {
    "source": "result.certificates.origin"
}

result = translate(template, source)

print(f"result: {result}")


