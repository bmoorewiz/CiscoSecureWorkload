# tetration
These are scripts that I use on the Cisco Tetration platform. 

------------------------------------------------------------------------------------------------------------------------------
Create Scopes Python
This requires the tetpyclient; pip install tetpyclient

This code will take a CSV file named on line 7 that has hostname contains query data in column 0 and scope name in column 1.
apps.csv
web Web Servers
DB Database Servers
The above .csv would create 2 scopes named Web Servers and Database Servers that the hostname contained web or db in it. 

Additionally the parent_app_scope_id on line 30 needs to be defined, this can be found in the GUI by clicking on the scope and looking at the ID in the URI. 

Type:contains on line 26 can be changed to eq or other regex expressions to match your need. The field value on line 27 can match any of the Tetration fields of your choosing.

This is particularly useful script when you have thousands of scopes to create as I did.

------------------------------------------------------------------------------------------------------------------------------
