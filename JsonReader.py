import json


json_string = '''
{
  "username" : "my_username",
  "password" : "my_password",
  "validation-factors" : {
      "validationFactors" : [
         {
            "name" : "remote_address",
            "value" : "127.0.0.1"
         }
      ]
  }
}
'''

#Loads is used to load string data into dict 
data = json.loads(json_string)
print(type(data))

print(data.keys())

del data['password']

#dumps is used to dump json ata to String format     
newjson_String = json.dumps(data)
print(newjson_String)
print(type(newjson_String))


#Use of load to load json file into  python object format
mydata=None
with open('myrequest.json','r') as file:
    mydata = json.load(file)
    print(mydata)
    
del mydata['display-name']


    json.dump(mydata,file)
with open('new_myrequest.json','w') as file :