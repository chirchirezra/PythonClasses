import json

with open("config.json") as json_file:
    json_data = json.load(json_file)
   # print(json_data)
json_data['db_host'] = "localhost"
json_data['db_name'] = "WorkingWithPythonClasses"
json_data['db_user'] = "root"

with open("config.json",'w') as  fw:
    
    json.dump(json_data,fw)
