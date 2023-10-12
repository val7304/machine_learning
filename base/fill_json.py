import json

mydict = {
     "component": {
       "key": "CSDR-AUTORESPONDER-PARENT",
       "name": "autoresponder-parent",
       "qualifier": "TRK",
       "measures": [
         {
           "metric": "coverage",
           "value": "50.8",
         },
         {
           "metric": "new_coverage",
           "value": "0",
         }
         
       ]
     }
   }




#create and save an dictionnaire file in json
json_string = json.dumps(mydict, indent=4)
with open('fill_data.json', 'w') as f:       #use a for append
    f.write(json_string)
    
#E:\workspace\python\sonar\source\jpr.json 