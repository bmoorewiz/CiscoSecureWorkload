from pprint import pprint
import sys
import json
from tetpyclient import RestClient

#Tetration IP address
API_ENDPOINT="https://10.0.76.4"
searchString = str(sys.argv[1])
#auth
restclient = RestClient(API_ENDPOINT, credentials_file='credentials.json', verify=False)
#GET
resp = restclient.get('/app_scopes')
#Turn Resp into python list
parsed_resp = resp.json()

#Iterate through JSON response for searchString and Print name and short_name, id, and query are also options among others
for s in range(len(parsed_resp)):
    if searchString in parsed_resp[s]["name"]:
        print(parsed_resp[s]["name"] + ' ID: ' + parsed_resp[s]["id"])