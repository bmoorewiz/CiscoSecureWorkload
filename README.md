# Cisco Secure Workload (Tetration)
These are scripts that I use on the Cisco Tetration platform, the Usage section applies to all scripts in this repository.

------------------------------------------------------------------------------------------------------------------------------
# Usage  
## Either clone the repository as below, or simply download the python files, included in the repository is sample credentials and csv files. You must use your own or modify the ones in the repository.  
git clone https://github.com/bmoorewiz/CiscoSecureWorkload  
## install tetpyclient  
pip install tetpyclient  
## define csv file 
### On line 7 of CreateScopes.py  
## Define API_Endpoint with the Tetration IP address or hostname
### On line 6 of CreateScopes.py and on line 5 of SearchAgents.py
## run python, python 3 required  
python3 CreateScopes.py  

# All scripts also require a credentials.json file, instructions here: https://www.cisco.com/c/en/us/td/docs/security/workload_security/tetration-analytics/sw/config/b_Tetration_OpenAPI/m_OpenAPI_Authentication.html

------------------------------------------------------------------------------------------------------------------------------
# Create Scopes Python    
More Details  
This code will take a CSV file named on line 7 that has hostname contains query data in column 0(line 28) and scope name in column 1(line 24).  
appss.csv  
web Web Servers  
DB Database Servers  
The above .csv would create 2 scopes named Web Servers and Database Servers that the hostname contained web or db in it.  

Additionally the parent_app_scope_id(line 30 & 10) needs to be defined, this can be found in the GUI by clicking on the scope and looking at the ID in the URI.   

Type:contains on line 26 can be changed to eq or other regex expressions to match your need. The field value on line 27 can match any of the Tetration fields/annotations of your choosing. Most of this can be found here: https://www.cisco.com/c/en/us/td/docs/security/workload_security/tetration-analytics/sw/config/b_Tetration_OpenAPI/m_inventory.html  

This is particularly useful script when you have thousands of scopes to create as I did.  

------------------------------------------------------------------------------------------------------------------------------
# Search Agents Python  
More Details  
This python code will take a search string located on line 6 and search for any host in the scopes named on line 12 and return all agents matching that string. The exact boolean strings such as contains or eq or the fields such as hostname or other annotations can be changed on line 17.   
Line 26 can return any json keys or annotations assigned to the filtered endpoints, currently it returns IP and hostname.   

------------------------------------------------------------------------------------------------------------------------------
