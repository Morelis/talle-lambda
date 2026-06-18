import json
from bodyResponse import bodyresponse


def lambda_handler(event, context):
   
    return bodyresponse (200 , "Hello from lambda, con SAM !!")
    

