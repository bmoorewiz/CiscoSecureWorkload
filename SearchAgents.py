import json
from tetpyclient import RestClient

#Tetration IP address
API_ENDPOINT="https://x.x.x.x"
searchFilter = "web"
#auth
restclient = RestClient(API_ENDPOINT, credentials_file='credentials.json', verify=False)
#Payload
req_payload = {
    #ScopeNames Below, you can have multiple, or just one
   "scopeName": "Default", "Default:HCA:XRDC"
   "limit": 2,
   "filter": {"type": "and",
      "filters": [
          #Hostname is just one of any field you can search on, contains can be any of the boolean values
         {"type": "contains", "field": "hostname", "value": searchFilter}
      ]
   }
}
resp = restclient.post('/inventory/search', json_body=json.dumps(req_payload))
print(resp.status_code)
if resp.status_code == 200:
   parsed_resp = resp.json()
   for results in parsed_resp["results"]:
      print(results["host_name"], results["ip"])
