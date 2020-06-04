def is_type(value, *args):
    return type(value) in args
    
def query_field_value(path, source):        
    result = dict(source)
    for key in list(path):                    
        if isinstance(result, dict) and key in result:                
            if key == path[-1]:                    
                return result[key]
            else:
                result = result[key]
                path.remove(key)
        elif isinstance(result, list):                                            
            return query_field_value(path, result[0])
        else: 
            return None
    return None 

def get_value(field, source):
    return source[field] if field in source else None