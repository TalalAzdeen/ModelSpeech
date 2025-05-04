import gradio as gr
SECRET_KEY_CORE = "https://modelspeech.onrender.com" #key
from enum import Enum, auto
import base64
import hmac
import hashlib
import requests
import json



def base64url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=')

def create_jwt(header, payload, secret_key):
    try:
        header_json = json.dumps(header, separators=(',', ':')).encode()
        payload_json = json.dumps(payload, separators=(',', ':')).encode()

        header_b64 = base64url_encode(header_json)
        payload_b64 = base64url_encode(payload_json)

        signing_input = f"{header_b64.decode()}.{payload_b64.decode()}".encode()

        signature = hmac.new(secret_key.encode(), signing_input, hashlib.sha256).digest()
        signature_b64 = base64url_encode(signature)

        jwt_token = f"{header_b64.decode()}.{payload_b64.decode()}.{signature_b64.decode()}"
        return jwt_token



    except Exception as e:
        return {"error": str(e)}

def base64url_decode(data):
    """Decode base64 URL-safe string"""
    padding = '=' * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)

def verify_jwt_signature(jwt_token, secret_key):
    """Verify the signature of a JWT token using HMAC-SHA-256"""
    try:
        # Split JWT into parts
        header_b64, payload_b64, signature_b64 = jwt_token.split('.')

        # Decode header and payload
        header = json.loads(base64url_decode(header_b64).decode())
        payload = json.loads(base64url_decode(payload_b64).decode())

        # Compute the expected signature
        signing_input = f"{header_b64}.{payload_b64}".encode()
        expected_signature = hmac.new(secret_key.encode(), signing_input, hashlib.sha256).digest()

        # Decode provided signature
        provided_signature = base64url_decode(signature_b64)

        # Verify the signature
        if hmac.compare_digest(provided_signature, expected_signature):
            return {"valid": True, "header": header, "payload": payload}
        else:
            return {"valid": False, "error": "Invalid signature"}

    except Exception as e:
        return {"valid": False, "error": str(e)}
class AuthSessionState(Enum):
    SUCCESS = auto()
    INVALID_TOKEN = auto()
    EXPIRED_TOKEN = auto()
    TOKEN_CREATION_FAILED = auto()
    NO_API_URL = auto()
    API_REQUEST_FAILED = auto()
    RESPONSE_TOKEN_INVALID = auto()


class AuthSessionBuilder:
    def __init__(self, secret_key):
        self.secret_key = secret_key



    def create_token(self, header, payload, secret_key):

        return create_jwt(header, payload, secret_key)

    def validate (self, token):
        statedata = verify_jwt_signature(token,self.secret_key)
        if not statedata['valid']:

            return {'state':AuthSessionState.INVALID_TOKEN}
        payload=statedata['payload']
        header =statedata['header']

        url = payload.get("ApiUrl")


        if not url:
            print("No API URL found in token payload!")
            return {'state':AuthSessionState.NO_API_URL}


        secret_key=payload.get("WebToken")
        payload['tokenCore']=self.secret_key

        token_val = self.create_token(header, payload, secret_key)

        if not token_val:
            print("Failed to create a new token!")
            return {'state':AuthSessionState.TOKEN_CREATION_FAILED}

        state, valdata = self.send_to_api(url, token_val)
        if not state:
            print("Failed to validate token with external API!")
            return {'state':AuthSessionState.API_REQUEST_FAILED}


        url="https://lahja-api.runasp.net"
        return {'state':AuthSessionState.SUCCESS,'token':valdata,"urlapi":url,"data":payload.get("data")}

    def send_to_apii(self, url, token):

        """إرسال التوكن إلى API خارجي والتحقق من الاستجابة"""
        try:
            response = requests.post(url, json={"token": token}, timeout=5)
            response.raise_for_status()
            return True, response.json().get("token")
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return False, None
    def send_to_api(self, url, token):

          """إرسال التوكن إلى API خارجي والتحقق من الاستجابة"""
          try:


              headers = {
                        "accept": "text/plain",
                        "Content-Type": "application/json"
                    }
              data = {
                # "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTZXNzaW9uVG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKVGRHRnlkRVJoZEdVaU9pSTFMekV2TWpBeU5TQTVPakF6T2pVNElGQk5JaXdpWlhod0lqb3hOelEyTVRNek16ZzJMQ0pwYzNNaU9pSnBjM04xWlhJaUxDSmhkV1FpT2lKb2RIUndjem92TDJ4dlkyRnNhRzl6ZERvM01EQXpJbjAucXJuYk90WExrVFNOQlVocVRSS0JKaDVWX0VLTVZsM1Ayd1UyOVdUQ2RBcyIsImV4cCI6MTc0NjIxOTg2NiwiaXNzIjoiaXNzdWVyIiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NzAwMyJ9.iKzZ7yIFZv4EiE8WvmeNCnt4ap1mZyaV856jFz_MMGM"
                    "token":token
                }

              response = requests.post(url, json=data)
              response.raise_for_status()
              return True, response.json().get("token")
          except requests.exceptions.RequestException as e:
              print(f"API request failed: {e}")
              return False, None


class AuthSessionBuilderSeed:
      def validate (self, token):
          url="https://lahja-api.runasp.net"
          return {'state':AuthSessionState.SUCCESS,'token':token,"urlapi":url,"data":None}


def cheack_token(token):

    return True

def  get_appsetting():
     data={
          "token":"""CfDJ8N119lGP1LJGlWWZ1xdZ5G_nrtYch9EvDSss0qDbsZbWYGaw_Jl0pV2QD-TEVct2S3kll3Czwn9Udh3vXUEjQ9c9tCjnOcxEEXQuAWPe-0FzPLWlM2Sis7SbG67r2QH4_bmynnxV_8ze6QBnk9ABGcD0_cy5ExoShStnINZrGMwosmDbq-i9iXw6giiulRQNKGimFyHtBPTAML7QeUMkxh1wYNezIBniw3dliEtH8TsUYDsSxMgjKcmAEbT__bAACKx9EX7F1muia80oLJAgGyYLABSRZPrucG190xdtIuRwugm3pmIjBtyptFGi46lSISSsdH2uMzpz8TO5wleoYrsjEmBMWkLgaYSxcHt6EFP4VyQMa5cG-nOese5YrKysmWWlcXL3KONp2lv62sPT8CdkOAnDp6W7VQvUB-Z98WRZYHj_57JuLAfg8IRhe61e3lD5QQZVGnI4SqdPlAtZrDUi-PsJqDa-T8s8tq63vhdrXtI_EUiavuU75-PbcCVse3KjCyOzjzxpXN3ELeWWcVTQJfIZuH531wtSInGF3l_TG2vHzwR_0O_HxejqdIj_W2wGkWSyW-_y_upg1rtsKpRhD15yiVIKpWm_1-zvlUETIgvbumNhPsThQaknE6KVYkJ3Uk1yGxxAx-ZPr8lzX6SQCVnPVi4kljrsl3UQ-2fVWq0NpdAW3xt_eBHMYis1HQIdCbQUWFIYfGERDoSoxEDFcynymOj1axSeUCxzHpF4J8okEuC3jbdmK2ytFjqejwUTsAMvd1a_7MpOt-ZCZ1_pDK4KJd2vh-Hm-3o7jRUcM35ee7JGCfEBTbel-oeis8rRDxm-y-GrZRgnT1snbi2nsyU_3F_R4FpUlypPGjzkiFcLIw5GW7zuw0zYzhDg_2Xt8ftNJCwQHdZRc2hCJn0e7EGJkl0q59H1xca7sYQ2""",
         "lg":"ar",
         "data":None,
          'url_redirect':'',
          'url_cancel':''

         }
     return data



class  APPException:
     def  catchwithAuth(self,message=""):

          return True

     def  catchwithAuthUI(self,message=""):

        print("#خطا في المصادقة")
         #gr.Markdown("#خطا في المصادقة")

     def catchStartUp(self,message):
          #gr.Markdown("## هنا استدعاء  دالة  اعاده التوجية  او رسالة خطا او اي شي ")
          gr.Markdown(message)








Request_WEB=['url_redirect','url_cancel','data']
def get_web_dataurl(querys):
    ds={}
    for sw in  Request_WEB:
      if sw in querys:
        ds[sw]=querys[sw]

    return ds

def  create_api(tamplate,isDev=True,inputs=[],outputs=[],exception=APPException()):
         return  tamplate("","",isDev).createapi(data=[])


def  create_app(tamplate,isDev=True,inputs=[],outputs=[],exception=APPException()):

     with gr.Blocks() as demo:
          state=gr.State(value=None)

          @gr.render()
          def main(request: gr.Request):

              if    isDev==False:
                  if request:
                     appsettingdata=dict(request.query_params)
                     # اذا كنت لم تستخدم الرابط وتضيف له التوكن
                     if len(appsettingdata)==0:
                        # هذا تنشه  من  api create AuthorizationSession
                        token_session="""eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTZXNzaW9uVG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKcWRHa2lPaUpoTlRRNVkyWXpNaTFoTnprNUxUUmhORFF0WVRrMFlpMHlOVGRrTTJFNE9HUTJNMklpTENKbGVIQWlPakUzTkRrd05ERXdNVGtzSW1semN5STZJbWx6YzNWbGNpSXNJbUYxWkNJNkltaDBkSEJ6T2k4dmJHOWpZV3hvYjNOME9qY3dNRE1pZlEuSlh4Q01hbGtmMHJnUHpEOVh2OERPNXlkWEwxdi1TR21XMnA0LXNVaWozbyIsIkFwaVVybCI6Imh0dHBzOi8vbGFoamEtYXBpLnJ1bmFzcC5uZXQvYXBpL3YxL3VzZXIvQXV0aG9yaXphdGlvblNlc3Npb24vdmFsaWRhdGUiLCJXZWJUb2tlbiI6IjM3MTNhYjdmNzkxYzE5OTFkM2EyMTBjNWZhNjhjNWFhIiwiRGF0YSI6IntcIlNlc3Npb25JZFwiOlwic2Vzc18yN2NhNmI2YjcxMWM0YWQ1YjlmZmNmZWEwNjUyMWJkZVwiLFwiU3Vic2NyaXB0aW9uSWRcIjpudWxsLFwiU2VydmljZXNcIjpbe1wiSWRcIjpcInNlcnZfODI4NDYzMTA3OWNjNDBmZjhmYjhhZmExNWRkODZkY2RcIixcIkFic29sdXRlUGF0aFwiOlwic3R1ZGlvLXQyc3BlZWNoXCJ9XSxcIlNwYWNlXCI6e1wiSWRcIjpcInNwYWNlX2YwZGRkZGVkYmYxYzRkNGRhZGI4OTVhNWQ3NDYzMTk5XCIsXCJOYW1lXCI6XCJ0ZXN0XCJ9fSIsImp0aSI6IjAzYWNmNWZhLTgxNWYtNDM2YS1hMTI5LWMzYWEzMTI4NGM3OSIsImV4cCI6MTc0OTA0MTAxOSwiaXNzIjoiaXNzdWVyIiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NzAwMyJ9.jqkka8Bosdm4Mm0qm1F-jVW35ppV-ELBdrk-JzhD79Q"""

                        appsettingdata['token']=token_session
                        appsettingdata['lg']='ar'
                        appsettingdata['data']=None
                        appsettingdata['url_redirect']=''
                        appsettingdata['url_cancel']=''



              else:
                     print("Devlober")

                     appsettingdata=get_appsetting()
              try:


                   token_session=appsettingdata.pop("token")



                   print("Api Connect")

                   if cheack_token(token_session):

                      auth=AuthSessionBuilder(SECRET_KEY_CORE) if isDev==False else AuthSessionBuilderSeed()
                      # auth=AuthSessionBuilderSeed()
                      res=auth.validate(token_session)

                      if res['state'] != AuthSessionState.SUCCESS:
                           exception.catchwithAuth()
                           print(exception.e)
                           print("#خطا في المصادقة")

                      else:
                          print("#Token  successful ")
                          #token="""Bearer CfDJ8Hr3sPyh0OJGnuGNrgSdKHxHdNfonEDv0j3gjLnaovJ91wx6_arbOYO1FA3mUJ3DaJky_EL-hatDdmvSy6voElNyDHxdG6KfCDSTZ9CA8Msh4iLzaWPy_I3EYppWt8RulCzgqd8sgKO1gfOL5qJTKErdyLJboOOtH5vsVJTp1Z1ChMkqjbOYTnOQqn6qbJifxrRwl2l10Fnfrewyb_JsITsivCAs-2KSG42Mz615mkoJztTnRkUIFI_g8JPJV7yx9je_sIZK_fdMqu0CTGx5sMrdBH7DydLJm6ynu5a6IBvSYGZ-es46PacVodoGvxaFO4HwAe-_29KYtDnaSgeRkXTRONix1pimTx21OnEO18O02WcudiOKFbZCvUZKZzIQWk2ms_v7kwBXhGEv_aSy3Rn2KZb_vcey-k78QyG83HJ3PBsLrefWTH_svpSmlLeo9OngPtCVUmbiAImtUyqJz9cGPpOOYvWJhJYS3j0LPZGXt_JfFn-Wbd3ebgjlqxnPTZCpPSSvj99hDAT_vnxH4NFBl6hCpGTNv6uwzTvlFDaSYjEwNiu8NLR_pzbvc_voYdGB2L2t86dIyzTRvT8Oxu_lBswXd0q078fFH54iPtIzEB3bAXiwaP6YxJhNLvR45jAhr28NHVtjfFcroAdJRBx2iL8jps649pt7IO2PCAt2FcrogI7oOV_Cz_z1o3Y6D5tPACC6SO1Xc8tyt9z__T18OPSsYZgEZ4AN9QeYw72SHK13Be7xuywNuqhZIT7KZYLi4VbsADd2prHbIJhdUYNlkX3zw19ItdMAz3iY19P78_WrbDSaVTXhruJiqMD8onTrNES3sdiqEzXl8VomSVZ2IaZOFFPTBajEFoffsvTX6VK9XGgwhd3yNuo5EzJl9hvybwMZMBgcQPi6yr3pXIUuLUdY65WnIAQJhapqV89j"""
                          token=token ="Bearer " + res['token']

                          urlapi=res['urlapi']
                          lg=appsettingdata.pop("lg")

                          # اي بيانات
                          data={"api":res["data"],"web":get_web_dataurl(appsettingdata)}

                          tamplate(urlapi,token,isDev).createapp(data,lg)


                   else:
                          exception.catchwithAuthUI()
                          print("catchwithAuthUI")
              except Exception as e :
                    exception.catchStartUp(f"حدث خطأ: {e}")

          demo.load(fn=main, inputs=inputs, outputs=outputs)
          return demo

