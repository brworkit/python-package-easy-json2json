def query_source_field_value(path_array, source):
    source_copy = dict(source)
    for key in path_array:
        print(f"key: {key}")
        print(f"source_copy: {source_copy}")
        
        if isinstance(source_copy, dict) and key in dict(source_copy):
            source_copy = source_copy[key]
            print(f"new source_copy: {source_copy}")
            if key == path_array[-1]:
                print(f"RETURN VALUE")
                return source_copy            
        else: 
            break
                
    return None

source = { "kingdom": {"phylum": { "class": { "order": { "family": { "genus": { "species": ["MAMALS"] } } } } }} }    

path_array = ["kingdom", "phylum", "class", "order", "family", "genus", "species", "kind"]

result = query_source_field_value(path_array, source)

print(f"result: {result}")


