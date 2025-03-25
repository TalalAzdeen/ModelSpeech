
from .clients import *
from typing import List
from apps.base.DataDynamicModel import *

# class builderSpace:

#     def __init__(self,urlapi,token):


#         self.buider=SpaceAPI(urlapi,token)

    
#     def create_space(self,name, description, ram, cpu_cores, disk_space,isGpu, isGlobal, bandwidth,data):

#         try:

#             dataa=data['api']
#             dynamic_model_instance =DataDynamicModel(dataa).convert_to_dynamic_model()
#             print(f"dynamic_model_instance:{dynamic_model_instance}")
            
#             data ={
#                 "name": name,
#                 "description": description,
#                 "ram": ram,
#                 "cpuCores": 3, # cpu_cores error
#                 "diskSpace": disk_space,
#                 "isGpu": isGpu,
#                 "isGlobal": isGlobal,
#                 "bandwidth": bandwidth,
#                 "token":"string",
#                  "subscriptionId":dynamic_model_instance.subscriptionId

               
#             }

#             result=self.buider.create_space(data)
#             if result!=None:

#                 return result
#             else:
#                 print("Error creating space.")
#                 return None

#             return result

#         except ValueError as e:
#             return {
#                 "status": "failed",
#                 "data": None,
#                 "message": str(e),
#                 "status_code": 400
#             }

#         except Exception as e:
#             return {
#                 "status": "failed",
#                 "data": None,
#                 "message": "An error occurred while creating the space.",
#                 "details": str(e),
#                 "status_code": 500
#             }


#     def update_space(self, space_id, data):

#         try:



#             result=self.buider.update_space(space_id,data)
#             if result!=None:
#                 return result
#             else:
#                 print("Error updating space.")
#                 return None


#         except ValueError as e:
#             return {
#                 "status": "failed",
#                 "data": None,
#                 "message": str(e),
#                 "status_code": 400
#             }

#         except Exception as e:
#             return {
#                 "status": "failed",
#                 "data": None,
#                 "message": "An error occurred while updating the space.",
#                 "details": str(e),
#                 "status_code": 500
#             }

#     def get_data_space_by_id(self, space_id):
#         """Retrieve space data by ID and return a structured response"""
#         try:

#             result=self.buider.get_data_space_by_id(space_id)
#             if result!=None:
#                 return result
#             else:
#                 print("Error retrieving space data.")
#                 return None

#         except ValueError as e:
#             return {
#                 "status": "failed",
#                 "data": None,
#                 "message": str(e),
#                 "status_code": 400
#             }

#         except Exception as e:
#             return {
#                 "status": "failed",
#                 "data": None,
#                 "message": "An error occurred while retrieving the space data.",
#                 "details": str(e),
#                 "status_code": 500
#             }

class builderSpace:

    def __init__(self,urlapi,token):


        self.buider=SpaceAPI(urlapi,token)

    # def create_space(self,data):

    #     try:

    #         result=self.buider.create_space(data)
    #         if result!=None:

    #             return result
    #         else:
    #             print("Error creating space.")
    #             return None

    #         return result

    #     except ValueError as e:
    #         return {
    #             "status": "failed",
    #             "data": None,
    #             "message": str(e),
    #             "status_code": 400
    #         }

    #     except Exception as e:
    #         return {
    #             "status": "failed",
    #             "data": None,
    #             "message": "An error occurred while creating the space.",
    #             "details": str(e),
    #             "status_code": 500
    #         }

    def create_space(self,name, description, ram, cpu_cores, disk_space,isGpu, isGlobal, bandwidth,data):

            try:

                parsed_data=data['api']
                dynamic_model_instance = DataDynamicModel(parsed_data).convert_to_dynamic_model()
                 
                print(f"dynamic_model_instance:{dynamic_model_instance}")
                
                quary ={
                    "name":"sss",
                    "description": description,
                    "ram": ram,
                    "cpuCores": 3, # cpu_cores error
                    "diskSpace": disk_space,
                    "isGpu": isGpu,
                    "isGlobal": isGlobal,
                    "bandwidth": bandwidth,
                    "token":"string", 
                    "subscriptionId":dynamic_model_instance.SubscriptionId

                  
                }
 
                result=self.buider.create_space(quary)
                if result!=None:

                    return result
                else:
                    print("Error creating space.")
                    return None

                return result

            except ValueError as e:
                return {
                    "status": "failed",
                    "data": None,
                    "message": str(e),
                    "status_code": 400
                }

            except Exception as e:
                return {
                    "status": "failed",
                    "data": None,
                    "message": "An error occurred while creating the space.",
                    "details": str(e),
                    "status_code": 500
                }

    def update_space(self,name, description, ram, cpu_cores, disk_space,isGpu, isGlobal, bandwidth,data):

        try:


                  parsed_data=data['api']
                  dynamic_model_instance = DataDynamicModel(parsed_data).convert_to_dynamic_model()
                      
                  print(f"dynamic_model_instance:{dynamic_model_instance}")
                      
                  quary ={
                          "name":"ss",
                          "description": description,
                          "ram": ram,
                          "cpuCores": 3, # cpu_cores error
                          "diskSpace": disk_space,
                          "isGpu": isGpu,
                          "isGlobal": isGlobal,
                          "bandwidth": bandwidth
                          

                        
                      }
                  #space_id=dynamic_model_instance.Id
                
                  #print(f"space_id:{space_id}")
                  result=self.buider.update_space("space_6dac9af4a71b408fbe1970212e052a43",quary)
                  return result



            
            
        except Exception as e:


                  return {
                      "status": "failed",
                      "data": None,
                      "message": "An error occurred while updating the space.",
                      "details": str(e),
                      "status_code": 500
                  }



    def get_data_space_by_id(self, space_id):

        """Retrieve space data by ID and return a structured response"""
        try:

            result=self.buider.get_data_space_by_id(space_id)
            if result!=None:
                return result
            else:
                print("Error retrieving space data.")
                return None

        except ValueError as e:
            return {
                "status": "failed",
                "data": None,
                "message": str(e),
                "status_code": 400
            }

        except Exception as e:
            return {
                "status": "failed",
                "data": None,
                "message": "An error occurred while retrieving the space data.",
                "details": str(e),
                "status_code": 500
            }
