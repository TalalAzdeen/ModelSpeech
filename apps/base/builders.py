from .clients import *
from .seeds import  RequestDev
from .DataDynamicModel import *

class BuilderRequest:
    def __init__(self, Url, Token, IsDev=True, max_dev_requests=2):
        """  Initialize the request builder with API or dev mode"""
        if IsDev:
            self.builder = RequestDev(max_dev_requests)
        else:
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



     
  
    def send_create_request_quary(self,quary):
        
        data=quary['api']
        

     
            

       
              
            
        dynamic_model_instance = DataDynamicModel(data).convert_to_dynamic_model()
           
        print(f"DataDynamicModel{dynamic_model_instance}")
        #if dynamic_model_instance.Spaces==None



        return self.Create_request(
           value="string",
           spaceid="space_001fc819a6ae4492be877f2869a3cbd3",
           serviceId=dynamic_model_instance.SubscriptionId

        
      
        )
    
        
        
 
    def send_event_request_quary(self,data,request,result,status_code):
         
           event_id=request["data"]["eventId"]
                     
           status=request["status"]
           return self.send_event_request(event_id,result,status)



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
                    "result":result,
                    "status":status
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

              "value": value.strip(),
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


