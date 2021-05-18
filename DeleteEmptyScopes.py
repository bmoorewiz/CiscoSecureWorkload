import sys
import json
from tetpyclient import RestClient
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Tetration IP address
API_ENDPOINT="https://x.x.x.x"
searchString = str(sys.argv[1])
#auth using credentials.json file
restclient = RestClient(API_ENDPOINT, credentials_file='credentials.json', verify=False)
#GET
appScopes = restclient.get('/app_scopes').json()
#Iterate through JSON response for SearchStright and Print name and short_name, id, and query are also options among other
for s in appScopes:
    if searchString in s["name"]:
        req_payload = {
             "scopeName": s["name"], # optional
              "filter": {"type": "and",
                "filters": [
                  {"type": "subnet", "field": "ip", "value": "0.0.0.0/0"},
                 ]
          }
          }
        #Iterate through scopes that match the searchString and get the inventory count
        scopeInv = restclient.post('/inventory/count', json_body=json.dumps(req_payload)).json()
        #If  Inventory count is 0, delete scope and print name and id
        if scopeInv["count"] == 0:
            restclient.delete('/app_scopes/' + s["id"])
            print(s["name"] + ' ID: ' + s["id"] + ' Count:' + str(scopeInv["count"]) + ' Deleted')
            