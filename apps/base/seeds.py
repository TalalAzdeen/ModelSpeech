class RequestDev:
    def __init__(self, max_requests: int):
        """  Simulate requests in development mode"""
        self.max_requests = max_requests
        self.request_count = 0


    def  send_event_request(self,data):
      
         return  None
    def send_event_request(self, eventId, status, message):
        """Send an event request to the API"""
        dataa = {
                "eventId":"aaaaaaaagsdhghghghghgg",
                "status": status,
                "message": message
               }
        return {
                "status": "success",
                "data": dataa,
                "message": "success to connect to API",
                "details":"",
                "status_code":200
            }

    def create_request(self, data):
        """  Create a mock request"""
        data_return = {
            "modelGateway": "string",
            "modelAi": "wasmdashai/T2T",
            "service": "string",
            "token": "AIzaSyC85_3TKmiXtOpwybhSFThZdF1nGKlxU5c",
            "eventId": "string",
            "numberRequests": self.max_requests,
            "currentNumberRequests": self.request_count + 1
        }



        if self.request_count < self.max_requests:
            self.request_count += 1
            return {
                "status": "success",
                "data":data_return,
                "message": "success to connect to API",
                "details":"",
                "status_code":200
            }
            return data_return
        else:
             return {
                "status":"failed",
                "data":None,
                "message": "success to connect to API",
                "details":"",
                "status_code":602
            }
