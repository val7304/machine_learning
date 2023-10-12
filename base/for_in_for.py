import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import collections

r=requests.get("https://webgate.ec.europa.eu/devcc-sonarqube/api/components/tree?component=Compass_Corproate&ps=500",auth=('4be8658483e54041a05fe86c4c9be0daa3cd3659',''))
jr= json.loads(r.text)

new_line_coverage=[]
service=[]
allService = []
nocover= []
colors=[]
x={}
y={}

metricKeys = ["new_coverage", "new_line_coverage"]

for y in jr["components"]:
    pkey=y["refKey"]
   
    if not(pkey.endswith("ui")):
        # print(pkey)     #67 au total sans ui
        
        all  = pkey
        allService.append(pkey) 
        

        for i in metricKeys:
            url_1 = "https://webgate.ec.europa.eu/devcc-sonarqube/api/measures/component?component="+pkey.rstrip()+"&metricKeys="+i+"&"
            r=requests.get(url_1,auth=('4be8658483e54041a05fe86c4c9be0daa3cd3659',''))
            
            jpr=json.loads(r.text)
            
            name=jpr["component"]["name"]
            service.append(name)
            cov = []
           
            if len(jpr["component"]["measures"])==0:
                coverage="no value"
                cov.append(0)
                nocover.append(all)    
            else:
            
                if jpr["component"]["measures"][0]["metric"]==metricKeys[0]:
                    coverm = []
                    coverm.append(float(jpr["component"]["measures"][0]["period"]["value"]))
                    coverage=jpr["component"]["measures"][0]["period"]["value"]
                    cov.append(float(jpr["component"]["measures"][0]["period"]["value"]))
                    x[name]=float(jpr["component"]["measures"][0]["period"]["value"])
                    cov_temp = coverm.sort()
                                                
                if jpr["component"]["measures"][0]["metric"]==metricKeys[1]:
                    new_line_coverage.append(float(jpr["component"]["measures"][0]["period"]["value"]))
                    new_line_coverage.sort()
                    
                    # for u in range(len(new_line_coverage)):
                    #     Pourcentage = new_line_coverage[u]*cov[u]*100
                    #     new_line_coverage = Pourcentage
                    #     print(Pourcentage, new_line_coverage)
                    
                    # print(cov)
                    
                    # percentage_list = ["{:.2f}%".format(i * 100) for i in my_list]
                    # print(percentage_list)

sort_cov=collections.OrderedDict(sorted(x.items(), key=lambda item:item[1]))
cov_temp = sort_cov.values()
cov=sort_cov.values()
service=sort_cov.keys()



    # print(Pourcentage, new_line_coverage)
                    
# print(cov)
# print(new_line_coverage)


# for x in cov:
#     if x <= 30:
#         colors.append('#D81643')
#     elif x < 50: 
#         colors.append('#FF9933')
#     else:
#         colors.append('#009900')

N=len(service)      #33 instead 60(using old metricKeys, so 70 in total) = missing 27 services
ind=np.arange(N)

# print(len(cov), len(new_line_coverage))
mname = service
metrics = {
    'coverage': cov,
    'line_covered': new_line_coverage
    }

x = np.arange(len(mname))  # the label locations
width = 0.30  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(constrained_layout=True)

for attribute, measurement in metrics.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3, size=8, rotation=90)
    multiplier += 1
    
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('pourcentage covered')
ax.set_title('new_line_coverage using metric new_coverage')
 
ax.set_xticks(x + width, mname, rotation=90)
ax.legend(loc='upper left', ncols=2)
ax.set_ylim(0, 110)

plt.show()