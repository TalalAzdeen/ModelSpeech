

from typing import Dict, Any, List  # Import Dict from typing module
import json
from pydantic import BaseModel
class DataDynamicModel:
    def __init__(self, data: str):
        self.data = data
        self.parsed_data = self.parse_data(data)

    def parse_data(self, data: str) -> Dict[str, Any]:  # Dict type hint is now recognized
        """تحليل البيانات وتحويلها إلى قاموس"""
        try:
            return json.loads(data)
        except Exception as e:
            raise ValueError(f"Error parsing data: {str(e)}")

    def generate_dynamic_model(self, data_dict: Dict[str, Any]) -> BaseModel:
        """إنشاء نموذج ديناميكي بناءً على القاموس المدخل"""
        from pydantic import create_model

        model_fields = {}

        for key, value in data_dict.items():
            if isinstance(value, dict):
                # إذا كانت القيمة قاموس، يتم إنشاء نموذج فرعي له
                model_fields[key] = (self.generate_dynamic_model(value), ...)
            elif isinstance(value, list):
                # إذا كانت القيمة قائمة تحتوي على قواميس
                if value and isinstance(value[0], dict):
                    model_fields[key] = (List[self.generate_dynamic_model(value[0])], ...)
                else:
                    model_fields[key] = (List[Any], ...)
            else:
                model_fields[key] = (Any, ...)

        return create_model("DynamicModel", **model_fields)

    def convert_to_dynamic_model(self) -> BaseModel:
        """تحويل البيانات إلى نموذج Pydantic ديناميكي"""
        dynamic_model = self.generate_dynamic_model(self.parsed_data)
        return dynamic_model(**self.parsed_data)