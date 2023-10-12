# -*- coding:Utf-8 -*-
# https://www.youtube.com/watch?v=MILtbfrMGL4

import matplotlib.pyplot as plt
import numpy as np

# lambda: générateur de fonction en python
# f = lambda x,y : np.sin(x) + np.cos(x+y)

y = ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
              0.5, 2.8, 12.2, 18.9, 29.4, 30.9, 34.2, 34.5, 35.5, 36.3, 37.9, 
              43.3, 44.3, 45.8, 45.9, 46.8, 49.3, 51.7, 52.8, 53.0, 54.9, 57.2, 
              57.9, 62.5, 62.8, 68.5, 68.8, 70.1, 70.4, 70.8, 71.1, 71.4, 71.5, 
              71.8, 72.3, 72.9, 73.7, 76.1, 76.6, 77.2, 77.2, 77.2, 77.2, 79.2, 
              79.7, 81.5, 85.4, 89.4])

x = (['cc-cert-requester-backend', 'cc-config-library-writer', 
            'cc-external-communication-backend', 'cc-reports-generator-backend', 
            'cc-rule-based-task-details-backend', 'cc-service-task-ares-backend', 
            'cc-sync-compass-backend', 'cc-tls-config-lib', 'compass-demo-service-backend', 
            'mywp-notifications-middleware', 'process-navigator-service', 'springboot-starter-backend', 
            'cc-signature-backend', 'cc-my-tasks-service-backend', 'clock-backend', 'cc-sharepoint-backend', 
            'flex-builder-service', 'cc-conversation-backend', 'cc-taxonomy-service-backend', 'user-profile', 
            'portfolio-manager-service', 'dynamictask-actions-backend', 'cc-taskActions-backend', 
            'cc-regio-business-backend', 'cc-task-allocation-backend', 'process-centre-service', 
            'flex-service', 'cc-document-manager-backend', 'cc-rule-based-task-details', 'cc-babel-backend', 
            'cc-kafka-sse-bridge-backend', 'cc-bulk-service-backend', 'cc-process-pfm-details-backend', 
            'cc-kafka-oracle-bridge-backend', 'cc-task-details-backend', 'cc-sfc-broker-backend', 
            'cc-servicetask-client-backend', 'cc-reports-backend', 'autoresponder-parent', 
            'cc-internal-communication-backend', 'cc-decide-cisnet-backend', 'cc-process-provider-wave', 
            'cc-consultation-backend', 'cc-ta-cci-creator-backend', 'cc-esif-internal-consultations-backend', 
            'cc-embedded-configuration-lib', 'cc-notification-backend', 'cc-saga-lib-root', 'cc-task-provider-wave', 
            'cc-decide-decision-backend', 'cc-sfc-backoffice-backend', 'cc-decide-cons-drools-model-backend', 
            'cc-decide-decision-drools-model-backend', 'cc-esif-internal-consultations-drools-model-backend', 
            'cc-internal-communication-drools-model-backend', 'cc-internal-communication-reporting-backend', 
            'cc-regio-business-helper-backend', 'task-details-provider-camunda-root', 'cc-portfolio-provider-wave-backend', 
            'cc-camunda-optimize-backend'])

plt.hist(y, bins= 60)
plt.hist(x, bins= 100)
# plt.hist2d(y, x)
# plt.xlabel("ms")
# plt.ylabel("%")
# plt.colorbar()

# bins= nbre de sections que l'on veut avoir dans l'histgramme


# permet de voir la distribution des données avec lesquelles on travaille

# plt.hist(x[:,0])
plt.show()






# plt.plot([1, 2, 3, 4])
# or
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.ylabel('some numbers')
# plt.show()

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']
# ax.bar(categories, np.random.rand(len(categories)));

