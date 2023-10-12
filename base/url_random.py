import random

url1="https://api.abc.com/users/"
url2="?api_key=5632lkjgdlg&_format=_show"

for i in range(4): 
    num=random.randint(1000,10000) #you can change the range here for generating a random number
    url=url1+str(num)+url2
    # print(url)


# real test: 
import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import collections

metricKeys = ["coverage", "new_coverage"] 
service = []


pkey  = "eu.europa.ec.cc.cc-camunda-optimize-backend"
# add all pkeys
for i in metricKeys:
    url_1 = "https://webgate.ec.europa.eu/devcc-sonarqube/api/measures/component?component="+pkey.rstrip()+"&metricKeys="+i+"&"
    r=requests.get(url_1,auth=('4be8658483e54041a05fe86c4c9be0daa3cd3659',''))
    print("metricKey used:"+i, "url used:"+str(r))
      
    
    
    
    
    
    
    
    
# But, if you wanted to split at that exact place without knowing how it looks beforehand, 
# you can use regex as you know for sure that a ? is found after this number.

import re

url="https://api.abc.com/users/12345?api_key=5632lkjgdlg&_format=_show"
matches=re.split('\d+(?=\?)',url)
['https://api.abc.com/users/', '?api_key=5632lkjgdlg&_format=_show']

url1=matches[0]
url2=matches[1]

# print(url1, url2)