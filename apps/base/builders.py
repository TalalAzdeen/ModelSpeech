from .clients import *
from .seeds import  RequestDev
import json
from .AutoMapper import *
class BuilderRequest:
    def __init__(self, Url, Token, IsDev=True, max_dev_requests=2):
        """  Initialize the request builder with API or dev mode"""
        self.isdiv=IsDev
        if IsDev:
            self.builder = RequestDev(max_dev_requests)
        else:
            print(Token)
            self.builder = RequestAPI(Url, Token)
        self.msg_event = "Initialized request builder"

    # def handle_api_result(self,result):

    #     if result:
    #         if isinstance(result, dict) and "error" in result:
    #             msg_event = f"Request failed: {result['error']}"
    #             print(f"Request failed - Status: {result.get('status_code')}, Details: {result.get('details')}")
    #             return {
    #                 "status": "failed",
    #                 "message": result['error'],
    #                 "details": result.get('details', None),
    #                 "status_code": result.get('status_code', None)
    #             }
    #         else:
    #             msg_event = "Request successful"
    #             print(f"Request successful: {result}")
    #             return {
    #                 "status": "success",
    #                  "status_code":result.get('status_code'),
    #                  "data": result
    #             }
    #     else:
    #         msg_event = "Request returned no result"
    #         print("Request returned no result")
    #         return {
    #             "status": "no_result",
    #             "message": "Request completed, but no result returned."
    #         }



     

    def extract_service_data(self,res: dict, service_name: str) -> dict:
      """
      Extract serviceId and spaceId from the response based on the service name.

      :param res: Dictionary containing a 'data' key as a JSON string.
      :param service_name: The name to match with the 'AbsolutePath' of a service.
      :return: Dictionary containing 'question', 'spaceid', and 'serviceId'.
      """
      try:
          # Parse the JSON string into a dictionary
          data_dict = json.loads(res)
          
          # Extract Space and Services information
          spaces = data_dict['Space']
          services = data_dict['Services']
          
          # Find the matching service
          for service in services:
              if service.get('AbsolutePath') == service_name:
                  return {
                      "question": "string",
                      "spaceid": spaces['Id'],
                      "serviceId": service['Id']
                  }

          # Raise error if the service is not found
          raise ValueError(f"Service with name '{service_name}' not found.")

      except (KeyError, json.JSONDecodeError, TypeError) as e:
          raise ValueError(f"Error processing data: {e}")

  
    def send_create_request_quary(self,data,nameT):
        
        if self.isdiv==False:
              d=data['api']
              
              data=self.extract_service_data(d,nameT)
              print(data)
              first_service_id =data["serviceId"]
              space_id = data["spaceid"]
              return self.Create_request(
                value="string",
                spaceid=space_id, 
                serviceId=first_service_id
              #  serviceId=dynamic_model_instance.SubscriptionId

              
            
              )
             #   data = quary['api']
    
# # إنشاء كائن  
#               fixed_data = fix_json_format(api_data)
#               print(fixed_data)
#               dynamic_model_instance =DataDynamicModel(fixed_data).convert_to_dynamic_model()
#               print(dynamic_model_instance)
#               service_ids = [service.Id for service in dynamic_model_instance.Services]
#               spaceid=dynamic_model_instance.Space.Id
#                 session_id = data["SessionId"]
#                 subscription_id = data["SubscriptionId"]
#                 first_service_id = data["Services"][0]["Id"]
#                 space_id = data["Space"]["Id"]

# # طباعة النتائج
#                 print("Session ID:", session_id)
#                 print("Subscription ID:", subscription_id)
#                 print("First Service ID:", first_service_id)
#                 print("Space ID:", space_id)
           
               
              #if dynamic_model_instance.Spaces==None
               
        else:
            print("false")
            return self.Create_request(

                value="string",
                spaceid="space_001fc819a6ae4492be877f2869a3cbd3",
                serviceId="dynamic_model_instance.SubscriptionId"

              
            
              )
        
        
 
    def send_event_request_quary(self,data,request,result,status_code):
           
           if self.isdiv==False:
                print(f"send_event_request_quary{request}")
                event_id=request["data"]["eventId"]   
                status=request["status"]
                return self.send_event_request(event_id,result,status)
           else:
                print("fff")
                event_id="space_001fc819a6ae4492be877f2869a3cbd3"  
                status="fffffff"
                return self.send_event_request(event_id,result,"rrrr")



    def send_event_request(self, event_id="",result="", status=""):
            try:
                if not isinstance(event_id, str) or not event_id:
                    return {"status": "failed", "message": "Invalid event_id. It should be a non-empty string."}

                if not isinstance(result, str) or not result:
                    return {"status": "failed", "message": "Invalid result. It should be a non-empty string."}

                if not isinstance(status, str) or not status:
                    return {"status": "failed", "message": "Invalid status. It should be a non-empty string."}

                data ={
                    "eventId":event_id,
                  
                    "status":status,
                    "details":result,
                }
                self.msg_event = "Sending send_event_request to create"
                result=self.builder.send_event_request(data)
                return result


            except Exception as e:
                  return {
                    "status": "failed",
                    "data":None,
                    "message":"An error occurred while processing the request.",
                    "details":str(e),
                    "status_code":0
                  }



    def Create_request(self, value="string",spaceid="", serviceId=""):
          """  Create a request and handle all possible return states, with input validation"""


          if not isinstance(value, str) or not value.strip():
              return {
                  "status": "failed",
                  "message": "Invalid value: Must be a non-empty string."
              }


          if not isinstance(spaceid, str) or not spaceid.strip():
              return {
                  "status": "failed",
                  "message": "Invalid spaceid: Must be a non-empty string."
              }

          if not isinstance(serviceId, str) or not serviceId.strip():
              return {
                  "status": "failed",
                  "message": "Invalid serviceId: Must be a non-empty string."
              }

          data = {

              "question": value.strip(),
               "spaceId":spaceid.strip(),
              "serviceId": serviceId.strip()
               }

          try:
              self.msg_event = "Sending request to create"
              result = self.builder.create_request(data)
              return result

          except Exception as e:


              self.msg_event = f"Error creating request: {e}"
              print(f"Error creating request: {e}")
              return {
                    "status": "failed",
                    "data":None,
                    "message":"An error occurred while processing the request.",
                    "details":str(e),
                    "status_code":0
                  }

from .clients import *
from typing import List
from .models import *
 
from .AutoMapper import *

class BuilderStudioModelAiAPi:
    def __init__(self, url: str, token: str) -> None:
        if not url or not token:
            raise ValueError("URL and Token must be provided.")
        self.Builder =SpeechStudioAPI(url, token)
        self.DataModels = None

    def get_filter(self, FilterModelAI, returnName: str) -> List[str]:
        if not returnName:
            raise ValueError("The returnName must be provided.")

        if not self.DataModels:
            try:
                result = self.Builder.get_filtered_models()
                
                print(result)

                if result and result.get("status") == "success"  :
                    json_data=result['data']['data']
                    fixed_data = fix_json_format(json_data)
                    data_model = DataDynamicModel(fixed_data)
                    transformed_data = data_model.transform_model_data()
                    self.DataModels = transformed_data
                    #self.DataModels = self.transform_model_data(result['data'])
                else:
                   #raise ValueError("No data returned from API.")
                   error=result.get("message")
                   print(f"Message event: {error}")
                   print()
                   return None
            except Exception as e:
                raise ValueError(f"Error while getting get filter  models: {e}")
                return None

        try:

            unique_values = {getattr(model, returnName) for model in self.DataModels if getattr(model, returnName) is not None}
        except AttributeError:
            #raise ValueError(f"Field '{returnName}' does not exist in the model data.")
            return None

        return list(unique_values)

    def transform_model_data(self, raw_data) -> List:
        if not raw_data or not isinstance(raw_data, list):
            raise ValueError("Invalid data format: raw_data should be a list of dictionaries.")

        transformed_list = []

        
        for item in raw_data:
            if not isinstance(item, dict):
                raise ValueError("Each item in raw_data must be a dictionary.")

            absolute_path = item.get('AbsolutePath', '')
            category = item.get('category', 'General').capitalize()  # Ensure category has a default value
            if category.lower() == 'ganaral':
                category = 'General'

            language = 'Arabic' if item.get('language', '').lower() == 'arabic' else 'English'
            dialect = item.get('dialect', '').replace('NAGD', 'Najdi Dialect') if item.get('dialect') else ''
            gender = 'Female' if item.get('gender', '').lower() == 'female' else 'Male'
            isStandard = item.get('isStandard', False)

            try:
                model = ModelAiCreate(
                    name=item.get('name', 'Unnamed Model'),
                    AbsolutePath=absolute_path,
                    category=category,
                    language=language,
                    isStandard=isStandard,
                    gender=gender,
                    dialect=dialect,
                    Type=item.get('type', 'Unknown')
                )
                transformed_list.append(model)
            except Exception as e:
                raise ValueError(f"Error creating model object: {e}")

        return transformed_list

    def get_property(self, field_name: str) -> List[str]:
        if not field_name:
            raise ValueError("The field_name must be provided.")

        return self.get_filter(FilterModelAI(), field_name)




# class TemplateBuilderRequest:
#     def __init__(self, Url, Token, IsDev=True, max_dev_requests=2):
#         """  Initialize the request builder with API or dev mode"""
#         if IsDev:
#             self.builder = RequestDev(max_dev_requests)
#         else:
#             self.builder = RequestAPI(Url, Token)
#         self.msg_event = "Initialized request builder"

#     # def handle_api_result(self,result):

#     #     if result:
#     #         if isinstance(result, dict) and "error" in result:
#     #             msg_event = f"Request failed: {result['error']}"
#     #             print(f"Request failed - Status: {result.get('status_code')}, Details: {result.get('details')}")
#     #             return {
#     #                 "status": "failed",
#     #                 "message": result['error'],
#     #                 "details": result.get('details', None),
#     #                 "status_code": result.get('status_code', None)
#     #             }
#     #         else:
#     #             msg_event = "Request successful"
#     #             print(f"Request successful: {result}")
#     #             return {
#     #                 "status": "success",
#     #                  "status_code":result.get('status_code'),
#     #                  "data": result
#     #             }
#     #     else:
#     #         msg_event = "Request returned no result"
#     #         print("Request returned no result")
#     #         return {
#     #             "status": "no_result",
#     #             "message": "Request completed, but no result returned."
#     #         }

#     def send_event_request(self, event_id="",result="", status=""):
#             try:
#                 if not isinstance(event_id, str) or not event_id:
#                     return {"status": "failed", "message": "Invalid event_id. It should be a non-empty string."}

#                 if not isinstance(result, str) or not result:
#                     return {"status": "failed", "message": "Invalid result. It should be a non-empty string."}

#                 if not isinstance(status, str) or not status:
#                     return {"status": "failed", "message": "Invalid status. It should be a non-empty string."}

#                 data = {
#                     "eventId":event_id,
#                     "result":result,
#                     "status":status
#                 }
#                 self.msg_event = "Sending send_event_request to create"
#                 result=self.builder.send_event_request(data)
#                 return result


#             except Exception as e:
#                   return {
#                     "status": "failed",
#                     "data":None,
#                     "message":"An error occurred while processing the request.",
#                     "details":str(e),
#                     "status_code":0
#                   }



#     def Create_request(self, value="string",spaceid="", serviceId=""):
#           """  Create a request and handle all possible return states, with input validation"""


#           if not isinstance(value, str) or not value.strip():
#               return {
#                   "status": "failed",
#                   "message": "Invalid value: Must be a non-empty string."
#               }


#           if not isinstance(spaceid, str) or not spaceid.strip():
#               return {
#                   "status": "failed",
#                   "message": "Invalid spaceid: Must be a non-empty string."
#               }

#           if not isinstance(serviceId, str) or not serviceId.strip():
#               return {
#                   "status": "failed",
#                   "message": "Invalid serviceId: Must be a non-empty string."
#               }

#           data = {

#               "value": value.strip(),
#                "spaceId":spaceid.strip(),
#               "serviceId": serviceId.strip()
#                }

#           try:
#               self.msg_event = "Sending request to create"
#               result = self.builder.create_request(data)
#               return result

#           except Exception as e:


#               self.msg_event = f"Error creating request: {e}"
#               print(f"Error creating request: {e}")
#               return {
#                     "status": "failed",
#                     "data":None,
#                     "message":"An error occurred while processing the request.",
#                     "details":str(e),
#                     "status_code":0
#    = self.generate_dynamic_model(self.parsed_data)
       

