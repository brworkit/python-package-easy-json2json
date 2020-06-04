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
        return field
    
    def query_source_field_value(self, path_array, source):
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


    def analyse(self, template: dict, source: dict):
        # print(f"template: {template}")
        # print(f"source: {source}")

        result = {}
        for field in template:
            _source_field_name = self.define_source_field_name(field, template)

            print(f"_source_field_name: {_source_field_name}")

            # if _source_field_name not in source:
            #     result[field] = self.property_not_found()
            # else:
            template_field_value = template[field]
            template_property_type = type(template_field_value)
            print(f"template_property_type: {template_property_type}")
            if template_property_type == dict:                    
                source_field_value = source[_source_field_name]
                source_field_value_type = type(source_field_value)                
                if source_field_value_type == list:
                    result[field] = []
                    for source_from_array in source_field_value:
                        result[field].append(self.analyse(template_field_value, source_from_array))
                elif source_field_value_type in [str, int, float]:
                    result[field] = self.fill_property(field, source, _source_field_name)
                else:
                    source_field_value = source[_source_field_name]                        
                    result[field] = self.analyse(template_field_value, source_field_value)
            elif template_property_type == list:
                source_field_value = self.query_source_field_value(template_field_value, source)                
                result[field] = source_field_value
            elif template_property_type == str:
                result[field] = self.fill_property(field, source, _source_field_name)

        return result

     
