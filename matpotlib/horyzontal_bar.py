# -*- coding:Utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# https://www.geeksforgeeks.org/draw-a-horizontal-bar-chart-with-matplotlib/



odict_values = ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 12.2, 18.9, 
                29.6, 30.9, 34.2, 34.5, 35.5, 36.3, 37.9, 43.3, 44.3, 45.8, 45.9, 46.3, 49.3, 
                51.4, 51.7, 52.8, 53.0, 54.9, 57.2, 57.9, 62.0, 62.8, 68.5, 68.8, 69.7, 70.4, 
                70.8, 71.1, 71.4, 71.5, 71.8, 72.3, 72.9, 73.7, 76.1, 76.6, 77.2, 77.2, 77.2, 
                77.2, 79.2, 79.7, 81.5, 85.4, 89.4])

odict_keys = (['cc-cert-requester-backend', 'cc-config-library-writer', 
                'cc-external-communication-backend', 'cc-reports-generator-backend', 
                'cc-rule-based-task-details-backend', 'cc-service-task-ares-backend', 
                'cc-sync-compass-backend', 'cc-tls-config-lib', 'compass-demo-service-backend', 
                'mywp-notifications-middleware', 'process-navigator-service', 
                'springboot-starter-backend', 'cc-signature-backend', 'clock-backend', 
                'cc-sharepoint-backend', 'flex-builder-service', 'cc-conversation-backend', 
                'cc-taxonomy-service-backend', 'user-profile', 'portfolio-manager-service', 
                'dynamictask-actions-backend', 'cc-taskActions-backend', 
                'cc-regio-business-backend', 'cc-task-allocation-backend', 
                'process-centre-service', 'flex-service', 'cc-document-manager-backend', 
                'cc-rule-based-task-details', 'cc-my-tasks-service-backend', 
                'cc-babel-backend', 'cc-kafka-sse-bridge-backend', 'cc-bulk-service-backend', 
                'cc-process-pfm-details-backend', 'cc-kafka-oracle-bridge-backend', 
                'cc-task-details-backend', 'cc-sfc-broker-backend', 
                'cc-servicetask-client-backend', 'cc-reports-backend', 
                'autoresponder-parent', 'cc-internal-communication-backend', 
                'cc-decide-cisnet-backend', 'cc-process-provider-wave', 
                'cc-consultation-backend', 'cc-ta-cci-creator-backend', 
                'cc-esif-internal-consultations-backend', 'cc-embedded-configuration-lib', 
                'cc-notification-backend', 'cc-saga-lib-root', 'cc-task-provider-wave', 
                'cc-decide-decision-backend', 'cc-sfc-backoffice-backend', 
                'cc-decide-cons-drools-model-backend', 'cc-decide-decision-drools-model-backend', 
                'cc-esif-internal-consultations-drools-model-backend', 
                'cc-internal-communication-drools-model-backend', 'cc-internal-communication-reporting-backend', 
                'cc-regio-business-helper-backend', 'task-details-provider-camunda-root', 
                'cc-portfolio-provider-wave-backend', 'cc-camunda-optimize-backend'])


line_coverage_keys = (['cc-config-library-writer', 'cc-external-communication-backend', 
                'cc-reports-generator-backend', 'cc-rule-based-task-details-backend', 
                'cc-service-task-ares-backend', 'cc-sync-compass-backend', 'cc-tls-config-lib', 
                'compass-demo-service-backend', 'mywp-notifications-middleware', 
                'process-navigator-service', 'springboot-starter-backend', 'cc-signature-backend', 
                'clock-backend', 'cc-sharepoint-backend', 'cc-cert-requester-backend', 
                'cc-conversation-backend', 'dynamictask-actions-backend', 'user-profile', 
                'cc-regio-business-backend', 'cc-taxonomy-service-backend', 'portfolio-manager-service', 
                'flex-builder-service', 'cc-rule-based-task-details', 'cc-task-allocation-backend', 
                'cc-my-tasks-service-backend', 'cc-kafka-oracle-bridge-backend', 'process-centre-service', 
                'cc-babel-backend', 'cc-task-details-backend', 'cc-document-manager-backend', 
                'cc-sfc-broker-backend', 'cc-kafka-sse-bridge-backend', 'cc-taskActions-backend', 
                'flex-service', 'cc-reports-backend', 'cc-embedded-configuration-lib', 
                'cc-decide-cisnet-backend', 'cc-esif-internal-consultations-backend', 
                'cc-consultation-backend', 'cc-bulk-service-backend', 'autoresponder-parent', 
                'cc-servicetask-client-backend', 'cc-ta-cci-creator-backend', 
                'cc-internal-communication-backend', 'cc-sfc-backoffice-backend', 
                'cc-internal-communication-reporting-backend','cc-decide-decision-backend', 
                'cc-regio-business-helper-backend','cc-decide-cons-drools-model-backend', 
                'cc-decide-decision-drools-model-backend', 'cc-esif-internal-consultations-drools-model-backend', 
                'cc-internal-communication-drools-model-backend', 'cc-process-pfm-details-backend', 
                'cc-saga-lib-root', 'task-details-provider-camunda-root', 
                'cc-notification-backend', 'cc-camunda-optimize-backend'])

# doit ajouter ce métric 
lines_covered_values = ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9, 18.3, 25.1, 
26.3, 40.7, 41.8, 45.4, 46.4, 46.5, 48.4, 51.6, 51.9, 53.7, 55.6, 57.3, 57.7, 59.4, 60.1, 
64.1, 65.3, 68.1, 69.5, 69.8, 70.1, 74.2, 75.5, 75.5, 75.9, 76.1, 79.2, 79.4, 79.5, 80.6, 
81.1, 81.3, 81.8, 83.1, 83.6, 83.6, 83.6, 83.6, 83.8, 85.8, 86.1, 87.1, 94.9])

# faire une boucle pour chaque metric
y=odict_keys
x= odict_values

print(len(y), len(x))   #metric coverage : 60, 60

# getting values against each value of y
lv = lines_covered_values
lk = line_coverage_keys
print(len(lv), len(lk))   #metric line_coverage: 57, 57

#search si compononent in line_coverage is in metric coverage
# if yes, take the indice[] value and past % number?/colore part line_covered/add the ligne above the component

fig = plt.figure(figsize=(30,20))
fig.subplots_adjust(bottom=0.100)

# add second metric for each y
plt.barh(lk, lv)
 
# setting label of y-axis
plt.ylabel("components")
 
# setting label of x-axis
plt.xlabel("Percentage covered")
plt.title("Old coverage Diagram - line covered")
plt.show()