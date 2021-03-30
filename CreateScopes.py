import json
from csv import reader
from tetpyclient import RestClient

#Tetration IP address
API_ENDPOINT="https://x.x.x.x"
csvName="apps.csv"
restclient = RestClient(API_ENDPOINT, credentials_file='credentials.json', verify=False)
#Scope ID's that are used most Frequently, the ID can be found in the GUI by clicking the scope and viewing the ID in the URI
defaultScope = "5b058fbe755f023c58c5a256"
testScope = ""

#Open CSV file
with open(csvName, 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        # Creates Scope with name of 2 column in each row, and the query value in the first column of each row, Parent Scope ID must aslo be set.
        # Parent Scope ID can be found in the GUI by clicking the parent scope, and then the ID is in the URI
        for row in csv_reader:
            req_payload = {
            "short_name": row[1],
            "short_query": {
            "type":"contains",
            "field":"host_name",
            "value": row[0]
                            },
            "parent_app_scope_id": defaultScope
                }
            resp = restclient.post('/app_scopes', json_body=json.dumps(req_payload))
            #print(resp.text) ##If Needed##
            #print(row[0],row[1]) ##Used to Print Test Rows to verify before pushing##
