# Cisco Secure Workload (Tetration)
These are scripts that I use on the Cisco Tetration platform, the Usage section applies to all scripts in this repository.

------------------------------------------------------------------------------------------------------------------------------
# Usage  
## Either clone the repository as below, or simply download the python files, included in the repository is sample credentials and csv files. You must use your own or modify the ones in the repository.  
    git clone https://github.com/bmoorewiz/CiscoSecureWorkload  
## install tetpyclient  
    pip install tetpyclient  
## Define API_Endpoint with the Tetration IP address or hostname
On line 6 of CreateScopes.py and on line 5 of SearchAgents.py please put a value for the IP address IE: API_ENDPOINT="https://1.1.1.1"

## run python (python 3 required)
    python3 CreateScopes.py
    python3 SearchAgents.py
    python3 SearchScopes.py ScopeFun <--Case sensitve search string
    python3 DeleteAgentsMatchingSearch.py 
    Python3 DeleteEmptyScopesPython.py Default:Scope1:

All scripts also require a credentials.json file, instructions here: https://www.cisco.com/c/en/us/td/docs/security/workload_security/tetration-analytics/sw/config/b_Tetration_OpenAPI/m_OpenAPI_Authentication.html

------------------------------------------------------------------------------------------------------------------------------
# Create Scopes Python
## Usage
### define csv file 
On line 7 of CreateScopes.py  

## More Details  
This code will take a CSV file named on line 7 that has hostname contains query data in column 0(line 28) and scope name in column 1(line 24).  
appss.csv  
web Web Servers  
DB Database Servers  
The above .csv would create 2 scopes named Web Servers and Database Servers that the hostname contained web or db in it.  

Additionally the parent_app_scope_id(line 10) needs to be defined, this can be found in the GUI by clicking on the scope and looking at the ID in the URI.   

Type:contains on line 26 can be changed to eq or other regex expressions to match your need. The field value on line 27 can match any of the Tetration fields/annotations of your choosing. Most of this can be found here: https://www.cisco.com/c/en/us/td/docs/security/workload_security/tetration-analytics/sw/config/b_Tetration_OpenAPI/m_inventory.html  

This is particularly useful script when you have thousands of scopes to create as I did.  

------------------------------------------------------------------------------------------------------------------------------
# Search Agents Python  
## More Details  
This python code will take a search string located on line 6 and search for any host in the scopes named on line 12 and return all agents matching that string. The exact boolean strings such as contains or eq or the fields such as hostname or other annotations can be changed on line 17.   
Line 26 can return any json keys or annotations assigned to the filtered endpoints, currently it returns IP and hostname.   

------------------------------------------------------------------------------------------------------------------------------
# Search Scopes Python  
## More Details  
This python code searches all scopes for full scopes names and returns anything that matches. Please note this is case sensitive. The first argument is used as the search string IE: python3 SearchScopes.py ScopeFun
Also, as usual, the IP address of the Tetration cluster is required as well as the credentials.json file. 

------------------------------------------------------------------------------------------------------------------------------
# Delete Agents Matching Search Python  
## More Details  
This python code searches the scopes on line 14 with the search filter from line 11 and then finds all agents that match that search filter on the cluster and permantently deletes them. Please be aware this cannot be undone. I use this to delete ISE agents that match host-. 
Also, as usual, the IP address of the Tetration cluster is required as well as the credentials.json file. 

------------------------------------------------------------------------------------------------------------------------------
# Delete Empty Scopes Python  
## More Details  
This python code searches the pattern you provide when running the python. For example "python3 DeleteEmptyScopes.py Default:Scope1:" This would delete any scopes in your scope tree that are BENEATH Scope1 and that also have 0 inventory items. This is good for large scale deployments where you have many scopes. 
Also, as usual, the IP address of the Tetration cluster is required as well as the credentials.json file. 

