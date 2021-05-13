import json
from tetpyclient import RestClient
import csv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Tetration IP address
API_ENDPOINT="https://x.x.x.x"
restclient = RestClient(API_ENDPOINT, credentials_file='credentials.json', verify=False)
#Search Filter, any agent whose hostname contains host- will be matched and deleted, host- typically means ISE agent. Change to fit your needs
searchFilter = "host-"
req_payload = {
    #ScopeNames Below, you can have multiple, or just one
   "scopeName": "Default", "Default:Scope1:Scope2"
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
count = 0
if resp.status_code == 200:
   parsed_resp = resp.json()
   for results in parsed_resp["results"]:
      #print(results["host_name"], results["ip"], results["host_uuid"])
      resp2 = restclient.delete('/sensors/' + results["host_uuid"])
      print(str(resp2.status_code), results["host_uuid"])
      count = count + 1
      print(count)


