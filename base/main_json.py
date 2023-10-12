import json

mydict = {
    "key": "CSDR-OPSYS-PAYMENT-FORECAST-BACKEND",
    "name": "'CSDR opsys-payment-forecast-backend'",
    "description": "J2EE, SpringMVC, eUI application",
    "qualifier": "TRK",
    "measures": [
         {
           "metric": "new_coverage",
           "periods": [
             {
               "index": 1,
               "value": "6.86274509803922",
               "bestValue": False
             }
           ],
           "period": {
             "index": 1,
             "value": "6.86274509803922",
             "bestValue": False
           }
         }
       ]
     },{
     "component": {
       "key": "CSDR-OPSYS-PAYMENT-FORECAST-BACKEND",
       "name": "'CSDR opsys-payment-forecast-backend'",
       "description": "J2EE, SpringMVC, eUI application",
       "qualifier": "TRK",
       "measures": [
         {
           "metric": "new_coverage",
           "periods": [
             {
               "index": 1,
               "value": "6.86274509803922",
               "bestValue": False
             }
           ],
           "period": {
             "index": 1,
             "value": "6.86274509803922",
             "bestValue": False
           }
         }
       ]
     }
     },{
     "component": {
       "key": "CSDR-OPSYS-PAYMENT-FORECAST-BACKEND",
       "name": "'CSDR opsys-payment-forecast-backend'",
       "description": "J2EE, SpringMVC, eUI application",
       "qualifier": "TRK",
       "measures": [
         {
           "metric": "new_coverage",
           "periods": [
             {
               "index": 1,
               "value": "6.86274509803922",
               "bestValue": False
             }
           ],
           "period": {
             "index": 1,
             "value": "6.86274509803922",
             "bestValue": False
           }
         }
       ]
     }
   },{
     "component": {
       "key": "CSDR-APP-SEDIA",
       "name": "app-sedia",
       "qualifier": "TRK",
       "measures": [
         {
           "metric": "coverage",
           "value": "0.0",
           "bestValue": False
         }
       ]
     }
   },{
     "component": {
       "key": "CSDR-APP-SEDIA",
       "name": "app-sedia",
       "qualifier": "TRK",
       "measures": [
         {
           "metric": "new_coverage",
           "periods": [
             {
               "index": 1,
               "value": "0.0",
               "bestValue": False
             }
           ],
           "period": {
             "index": 1,
             "value": "0.0",
             "bestValue": False
           }
         }
       ]
     }
   },{
     "component": {
       "key": "CSDR-AUTORESPONDER-PARENT",
       "name": "autoresponder-parent",
       "qualifier": "TRK",
       "measures": []
     }
   }




#create and save an dictionnaire file in json
json_string = json.dumps(mydict, indent=4)
with open('data.json', 'w') as f:       #use a for append
    f.write(json_string)
    
#E:\workspace\python\sonar\source\jpr.json 