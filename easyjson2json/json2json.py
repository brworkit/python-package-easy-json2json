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
            result = template[field]["_source"]
            del template[field]["_source"]
            return result
        else:            
            if type(template[field]) in [dict, list]:
                return field                
        return template[field]
    
    def query_field_value(self, path, source):        
        result = dict(source)
        for key in list(path):                    
            if isinstance(result, dict) and key in result:                
                if key == path[-1]:                    
                    return result[key]
                else:
                    result = result[key]
                    path.remove(key)
            elif isinstance(result, list):                                            
                return self.query_field_value(path, result[0])
            else: 
                return None
        return None 

    def read_list(self, template_field_value, source_field_value):
        result = []
        for source_from_array in source_field_value:
            result.append(self.analyse(template_field_value, source_from_array))
        return result

    def template_is_dict(self, field, template, source):
        source_field_name = self.define_source_field_name(field, template)                
        if type(source[source_field_name]) in [str, int, float]:
            return self.fill_property(field, source, source_field_name)
        
        template_field_value = template[field]
        if type(source[source_field_name]) == list:
            return self.read_list(template_field_value, source[source_field_name])
                                                                
        return self.analyse(template_field_value, source[source_field_name])

    def template_is_list(self, field, template, source):        
        return self.query_field_value(template[field] , source)

    def template_is_str(self, field, template, source):        
        source_field_name = self.define_source_field_name(field, template)
        return self.fill_property(field, source, source_field_name)

    def analyse(self, template, source):                
        result = {}
        for field in template:            
            if template[field] is None:
                result[field] = None
            else:                
                template_field_value = template[field]
                template_property_type = type(template_field_value)                            
                if template_property_type == dict:
                    result[field] = self.template_is_dict(field, template, source)
                elif template_property_type == list:                                                                
                    result[field] = self.template_is_list(field, template, source)
                elif template_property_type == str:
                    result[field] = self.template_is_str(field, template, source)
        return result

     
