### Importing pandas and TSC. 
### Whoever runs this will have to install tableauserverclient (pip install tableauserverclient)
import pandas as pd
import tableauserverclient as TSC

### Credentials to Tableau Server
username = input("Enter you SSO user: ")
password = input("Enter you SSO password: ")

### Login to Tableau Server
tableau_auth = TSC.TableauAuth(username, password)
server = TSC.Server('http://nymspr457.cusa.canon.com/', use_server_version=True)

server.auth.sign_in(tableau_auth)

### Dataframe with all flows in Tableau Server
flows_server = pd.DataFrame(columns=['Name', 'ID', 'Item'])

with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.flows.get()
    flow_names = [datasource.name for datasource in all_datasources]
    flow_ids = [datasource.id for datasource in all_datasources]

### Inputing flow info in the dataframe
flows_server['Item'] = all_datasources
flows_server['Name'] = flow_names
flows_server['ID'] = flow_ids

### Printing the name of every flow in the Server
print(flows_server['Name'])

### Input which flows to run
flows_selected = input("Enter all the flows you would like to run (separated by comma): ")

### Making a list with all the chosen names
selected_flows = [names.strip() for names in flows_selected.split(',')]

### Getting the item string for each chosen flow
selected_flow_items = flows_server[flows_server['Name'].isin(selected_flows)]['Item'].reset_index()
selected_flow_items.pop('index');

### Running wach chosen flow based on 'Item'
for i in range(0, len(selected_flow_items)):
    server.auth.sign_in(tableau_auth)
    server.flows.refresh(selected_flow_items.loc[i,'Item'])

### Signing out from Tableau Server
server.auth.sign_out()