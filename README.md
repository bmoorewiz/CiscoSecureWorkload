# Tetration
These are scripts that I use on the Cisco Tetration platform. 

------------------------------------------------------------------------------------------------------------------------------
Create Scopes Python
This requires the tetpyclient; pip install tetpyclient
It also requires a credentials.json file, instructions here: https://www.cisco.com/c/en/us/td/docs/security/workload_security/tetration-analytics/sw/config/b_Tetration_OpenAPI/m_OpenAPI_Authentication.html

This code will take a CSV file named on line 7 that has hostname contains query data in column 0(line 28) and scope name in column 1(line 24).
appss.csv
web Web Servers
DB Database Servers
The above .csv would create 2 scopes named Web Servers and Database Servers that the hostname contained web or db in it. 

Additionally the parent_app_scope_id(line 30 & 10) needs to be defined, this can be found in the GUI by clicking on the scope and looking at the ID in the URI. 

Type:contains on line 26 can be changed to eq or other regex expressions to match your need. The field value on line 27 can match any of the Tetration fields/annotations of your choosing. Most of this can be found here: https://www.cisco.com/c/en/us/td/docs/security/workload_security/tetration-analytics/sw/config/b_Tetration_OpenAPI/m_inventory.html

This is particularly useful script when you have thousands of scopes to create as I did.

------------------------------------------------------------------------------------------------------------------------------
