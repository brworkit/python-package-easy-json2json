from easyjson2json.helpers import *

class Json2Json(object):
    def __init__(self, template, source):
        super().__init__()
        self.__template = template
        self.__source = source
        self.__translated = None
        self._translate()

    def get_result(self):
        return self.__translated

    def _translate(self):
        self.__translated = self._analyse(self.__template, self.__source)
        return self.__translated

    def _get_source_field_name(self, field, template):        
        if "_source" in template[field]:            
            return template[field].pop("_source")
        elif is_type(template[field], dict, list):
            return field                                        
        return template[field]
    
    def _read_list(self, template_field_value, source_field_value):        
        return [self._analyse(template_field_value, source_from_array) for source_from_array in source_field_value]

    def _template_is_dict(self, field, template, source):
        source_field_name = self._get_source_field_name(field, template)                
        if is_type(source[source_field_name], str, int, float):
            return get_value(source_field_name, source)
        if is_type(source[source_field_name], list):
            return self._read_list(template[field], source[source_field_name])                                                                
        return self._analyse(template[field], source[source_field_name])

    def _template_is_list(self, field, template, source):        
        return query_field_value(template[field] , source)

    def _template_is_str(self, field, template, source):                
        return get_value(self._get_source_field_name(field, template), source)

    def _analyse(self, template, source):                
        result = {}
        for field in template:            
            if template[field] is None:
                result[field] = None
            else:                
                template_field_value = template[field]                
                if is_type(template_field_value, dict):
                    result[field] = self._template_is_dict(field, template, source)
                elif is_type(template_field_value, list):  
                    result[field] = self._template_is_list(field, template, source)
                elif is_type(template_field_value, str):
                    result[field] = self._template_is_str(field, template, source)                
        return result

     
