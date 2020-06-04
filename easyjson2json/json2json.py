class Json2Json(object):
    def __init__(self, template, source):
        super().__init__()
        self.template = template
        self.source = source
        self.translated = None
        self.translate()

    def translate(self):
        self.translated = self.analyse(
            self.template, source=self.source)
        return self.translated

    def get_result(self):
        return self.translated

    def get_value(self, property, source):
        return source[property] if property in source else None

    def property_not_found(self):
        return None

    def fill_property(self, field, source, _source_field_name=None):                
        return self.get_value(_source_field_name, source)

    def define_source_field_name(self, field, template):        
        if "_source" in template[field]:
            _source_field_name = template[field]["_source"]
            del template[field]["_source"]
            return _source_field_name
        else:
            array = field.split("|")
            if len(array) > 1:
                key = array[0]
                template[key] = template.pop(field)
                field = key
                return array[1]
            if isinstance(template[field], dict) or isinstance(template[field], list):
                return field
        return template[field]
    
    def query_source_field_value(self, path, source):        
        result = dict(source)
        for key in list(path):                    
            if isinstance(result, dict) and key in dict(result):
                result = result[key]                        
                if key == path[-1]:                    
                    return result
                path.remove(key)
            elif isinstance(result, list):                
                result = result[0]            
                return self.query_source_field_value(path, result)
            else: 
                break
        return None 


    def special_case(self, field, source, source_field_value, source_field_value_type, template_field_value, _source_field_name):                
        if source_field_value_type == list:
            result = []
            for source_from_array in source_field_value:
                result.append(self.analyse(template_field_value, source_from_array))
            return result
        elif source_field_value_type in [str, int, float]:
            return self.fill_property(field, source, _source_field_name)
        else:
            source_field_value = source[_source_field_name]                        
            return self.analyse(template_field_value, source_field_value)
    
    def extract_model(self, field, source):
        _model = source[field]["_model"] if "_model" in source[field] else None
        if _model:
            del source[field]["_model"]
        return _model

    def analyse(self, template: dict, source: dict):        
        result = {}
        for field in template:            
            if template[field] is None:
                result[field] = None
            else:
                _source_field_name = self.define_source_field_name(field, template)                
                print(f"field: {field}")
                print(f"_source_field_name: {_source_field_name}")            
                template_field_value = template[field]
                template_property_type = type(template_field_value)            
                print(f"template_property_type: {template_property_type}")
                if template_property_type == dict:                    
                    source_field_value = source[_source_field_name]
                    source_field_value_type = type(source_field_value)                                
                    result[field] = self.special_case(field, source, source_field_value, source_field_value_type, template_field_value, _source_field_name)
                elif template_property_type == list:                                            
                    source_field_value = self.query_source_field_value(template_field_value, source)                
                    result[field] = source_field_value
                elif template_property_type == str:
                    result[field] = self.fill_property(field, source, _source_field_name)
        return result

     
