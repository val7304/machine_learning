import json
import numpy as np
import matplotlib.pyplot as plt

service = []
cov = []
new_cov = []
nocover=0


with open(r"E:\workspace\python\sonar\source\jpr.json",'r') as f:
    json_object = json.loads(f.read())
    
    for i in range(len(json_object)):         
        name = (json_object[i]["component"]["name"])
        if name not in service:
            service.append(json_object[i]["component"]["name"])          
            
            if len(json_object[i]["component"]["measures"])==0:
                covm = 0
                # print("cov??",name, covm, "zero")
                # print("new_cov??",name, covm, "zero")
                new_cov.append(0.0)
                cov.append(0.0)

        if json_object[i]["component"]["measures"]:
            covm=json_object[i]["component"]["measures"][0]["metric"]

                # print(["rempli"],[name], json_object[i]["component"]["measures"])
            if covm=="coverage":
                covv = float(json_object[i]["component"]["measures"][0]["value"])
                # print("cov",name, float(json_object[i]["component"]["measures"][0]["value"])) 
                cov.append(float(json_object[i]["component"]["measures"][0]["value"]))
                
            if covm=="new_coverage":
                new_covv = float(json_object[i]["component"]["measures"][0]["period"]["value"])
                new_cov.append(float(json_object[i]["component"]["measures"][0]["period"]["value"]))
                    
                # print("new_cov",name, float(json_object[i]["component"]["measures"][0]["period"]["value"]))
            else:
                new_covv="vide"
        else:

           if covv >=0.0 and new_covv=="vide" and covm!=0:
                # print("new_cov??", name,"zero zero")
                new_cov.append(0.0)
            
           
 
# print("cov",len(cov),"new_cov", len(new_cov)) 
# print("service",len(service)) #176

mname = service
metrics = {
    'coverage': cov,
    'new_coverage': new_cov
}

x = np.arange(len(mname))  # the label locations
width = 0.40  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(constrained_layout=True)

for attribute, measurement in metrics.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=2, fontsize=8, rotation=90)
    multiplier += 1
    
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('pourcentage covered')
ax.set_title('coverage vs  metric new_coverage')
 
ax.set_xticks(x + width, mname, fontsize=6, rotation=90)
ax.legend(metrics, loc='upper left', ncols=2)
ax.set_ylim(0, 120)

plt.show()