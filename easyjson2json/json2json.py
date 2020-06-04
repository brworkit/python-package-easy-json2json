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

    def fill_property(self, field, source, _source_field_name=None):                
        return self.get_value(_source_field_name, source)

    def define_source_field_name(self, field, template):        
        if "_source" in template[field]:
            _source_field_name = template[field]["_source"]
            del template[field]["_source"]
            return _source_field_name
        else:            
            if isinstance(template[field], dict) or isinstance(template[field], list):
                return field
        return template[field]
    
    def query_field_value(self, path, source):        
        result = dict(source)
        for key in list(path):                    
            if isinstance(result, dict) and key in dict(result):
                result = result[key]                        
                if key == path[-1]:                    
                    return result
                path.remove(key)
            elif isinstance(result, list):                
                result = result[0]            
                return self.query_field_value(path, result)
            else: 
                break
        return None 

    def read_list(self, template_field_value, source_field_value):
        result = []
        for source_from_array in source_field_value:
            result.append(self.analyse(template_field_value, source_from_array))
        return result


    def solve_when_template_is_dict(self, field, template, source):
        source_field_name = self.define_source_field_name(field, template)
        source_field_value = source[source_field_name]
        source_field_value_type = type(source_field_value)                                                    
        if source_field_value_type == list:
            template_field_value = template[field]                        
            return self.read_list(template_field_value, source_field_value)
        elif source_field_value_type in [str, int, float]:
            return self.fill_property(field, source, source_field_name)
        else:                                     
            template_field_value = template[field]           
            return self.analyse(template_field_value, source_field_value)

    def analyse(self, template: dict, source: dict):        
        
        result = {}
        for field in template:            
            if template[field] is None:
                result[field] = None
            else:
                # source_field_name = self.define_source_field_name(field, template)                                
                template_field_value = template[field]
                template_property_type = type(template_field_value)                            
                if template_property_type == dict:
                    result[field] = self.solve_when_template_is_dict(field, template, source)
                elif template_property_type == list:                                            
                    source_field_value = self.query_field_value(template_field_value, source)                
                    result[field] = source_field_value
                elif template_property_type == str:
                    source_field_name = self.define_source_field_name(field, template)
                    result[field] = self.fill_property(field, source, source_field_name)
        return result

     
