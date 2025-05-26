import requests

class RequestAPI:
    def __init__(self, base_url, token):
        """Initialize API request class with base URL and token"""
        self.base_url = base_url
        self.headers = {
            "accept": "text/plain",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"  # Use Bearer token without spaces
        }


    def handle_response(self, response):
        """Handle API responses and format output"""
        if response.status_code in [200, 201]:
            return {
                "status": "success",
                "data": response.json(),
                "message": "Request processed successfully.",
                "details": "",
                "status_code": response.status_code
            }



        error_messages = {
            400: "Bad Request: Check the submitted data.",
            401: "Unauthorized: Check your token or permissions.",
            403: "Forbidden: You don't have access to this resource.",
            404: "Not Found: The requested item does not exist.",
            429: "Too Many Requests: Rate limit exceeded. Try again later.",
            600: "Custom Server Error: Something unexpected happened on the server."
        }

        if response.status_code >= 500:
            return {
                "status": "failed",
                "data": None,
                "message":response.text,
                "details": response.text,
                "status_code": response.status_code
            }

        return {
            "status": "failed",
            "data": None,
            "message":response.text,
            "details": response.text,
            "status_code": response.status_code
        }

    def send_event_request(self,data):
        """Send an event request to the API"""
        try:
            url = f"{self.base_url}/api/v1/user/Request/CreateEvent"


            response = requests.post(url, json=data, headers=self.headers)
            return self.handle_response(response)

        except requests.RequestException as e:
            return {
                "status": "failed",
                "data": None,
                "message": "Failed to connect to API",
                "details": str(e),
                "status_code": 0
            }

    def create_request(self, data):
        """Create a new request via API"""
        try:
            url = f"{self.base_url}/api/v1/user/Request"
            print(url)
            response = requests.post(url, json=data, headers=self.headers)
            return self.handle_response(response)

        except requests.RequestException as e:
            return {
                "status": "failed",
                "data": None,
                "message": "Failed to connect to API",
                "details": str(e),
                "status_code": 0
            }

            
class SpeechStudioAPI:
    __translation__ = {}

    def __init__(self, url, token) -> None:
        print("Initializing TamplateDashBuilder...")
        try:
            self.base_url = url
            self.token = token
            self.headers = {
            "accept": "text/plain",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"  # Use Bearer token without spaces
        }
            print("Builder initialized successfully.")
        except Exception as e:
            print(f"Error initializing builder: {e}")
            raise

    def get_filtered_models(self, payload):
        print("Sending request to GetFilterModel2 API...")
    
        url = f"{self.base_url}/api/v1/user/ModelAi/GetFilterModel?lg=en"
        # payload = {
        #     "name": name,
        #     "category":category,
        #     "language": language,
        #     "isStandard": isStandard,
        #     "gender": gender,
        #     "dialect": dialect,
        #     "type":Type
        # }
        return self._post_request(url, payload)

    def get_data_by_type(self, typee):
        return self._get_request("/api/ModelAi/ByType", {"type": typee})





    def _get_request(self, endpoint, params=None):
        url = f"{self.builder.url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        return self.handle_response(response)

    def _post_request(self, url, payload):
        response = requests.post(url, headers=self.headers, json=payload)
        return self.handle_response(response)



    def handle_response(self, response):
        """Handle API responses and format output"""
        if response.status_code in [200, 201]:
            return {
                "status": "success",
                "data": response.json(),
                "message": "Filter Model processed successfully.",
                "details": "",
                "status_code": response.status_code
            }

        error_messages = {
            400: "Bad  Get Filter Model Request: Check the submitted data.",
            401: "Unauthorized: Check your token or permissions.",
            403: "Forbidden: You don't have access to this resource.",
            404: "Not Found: The Filter Model item does not exist.",
            429: "Too Many Requests: Rate limit exceeded. Try again later.",
            600: "Custom Server Error: Something unexpected happened on the server."
        }

        if response.status_code >= 500:
            return {
                "status": "failed",
                "data": None,
                "message": "Server Error",
                "details": response.text,
                "status_code": response.status_code
            }

        return {
            "status": "failed",
            "data": None,
            "message": error_messages.get(response.status_code, "Unexpected Error"),
            "details": response.text,
            "status_code": response.status_code
        }


