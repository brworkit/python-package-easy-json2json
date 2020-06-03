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
        return {field: self.get_value(_source_field_name, source)}

    def analyse(self, template: dict, source: dict):
        print(f"template: {template}")
        print(f"source: {source}")

        result = {}
        for field in template:
            _source_field_name = field

            if "_source" in template[field]:
                _source_field_name = template[field]["_source"]
                del template[field]["_source"]
            
            print(f"_source_field_name: {_source_field_name}")

            if _source_field_name not in source:
                result[field] = self.property_not_found()
            else:
                template_field_value = template[field]
                property_type = type(template_field_value)

                if property_type == dict:
                    print(f"property_type: {property_type}")
                    source_field_value = source[_source_field_name]
                    source_field_value_type = type(source_field_value)
                    
                    print(f"source_field_value: {source_field_value}")
                    print(f"source_field_value_type: {source_field_value_type}")

                    if source_field_value_type == list:
                        result[field] = []
                        for source_from_array in source_field_value:
                            result[field].append(self.analyse(
                                template_field_value, source_from_array))
                    elif source_field_value_type == str:
                        result = self.fill_property(field, source, _source_field_name)
                    else:
                        source_field_value = source[_source_field_name]                        
                        result[field] = self.analyse(template_field_value, source_field_value)

                elif property_type == list:
                    source_field_value = source[_source_field_name]
                    result[field] = []
                    for array_template in template_field_value:
                        if type(array_template) == dict:
                            for source_from_array in source_field_value:
                                result[field].append(self.analyse(
                                    array_template, source_from_array))
                        else:
                            result = self.fill_property(field, source, _source_field_name)
                else:
                    result = self.fill_property(field, source, _source_field_name)

        return result
