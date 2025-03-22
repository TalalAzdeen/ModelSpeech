import json
from pydantic import BaseModel, create_model
from typing import Any, Dict, List

class DataDynamicModel:
    
    def __init__(self, raw_data: str):
        self.raw_data = self.parse_data(raw_data)

    def parse_data(self, data: str) -> List[Dict[str, Any]]:
        """تحليل البيانات وتحويلها إلى قائمة من القواميس"""
        try:
          
            parsed = json.loads(data)
            if not isinstance(parsed, list):
                raise ValueError("Invalid format: Expected a list of dictionaries.")
            return parsed
        except Exception as e:
            raise ValueError(f"Error parsing data: {str(e)}")



    def generate_dynamic_model(self, data_item: Dict[str, Any]) -> BaseModel:
        
        model_fields = {key: (Any, ...) for key in data_item.keys()}
        return create_model("ModelAiCreate", **model_fields)

    def transform_model_data(self) -> List[BaseModel]:
       
        if not self.raw_data:
            raise ValueError("No data provided for transformation.")

        dynamic_model = self.generate_dynamic_model(self.raw_data[0])
        return [dynamic_model(**item) for item in self.raw_data]

     
def fix_json_format(json_data) -> str:
            # Convert the list to a JSON string first
            json_string = json.dumps(json_data)  
            # Then replace single quotes with double quotes
            return json_string.replace("'", '"') 

        

 
 