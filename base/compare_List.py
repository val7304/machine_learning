cov = [50.8, 58.0, 53.0, 89.4, 19.6, 0.0, 71.1, 30.9, 70.4, 77.2, 76.1, 77.2, 47.0, 71.8, 71.0, 77.2, 0.0, 70.1, 77.2, 
       79.2, 57.2, 52.8, 2.9, 72.4, 54.9, 45.6, 79.7, 68.5, 0.0, 49.4, 0.0, 72.9, 0.0, 62.8, 77.4, 62.2, 18.8, 0.5, 0.0,
       71.4, 45.1, 30.0, 48.4, 34.2, 0.0, 12.4, 0.0, 36.3, 29.0, 46.0, 0.0, 36.3, 45.8, 0.0, 0.0, 81.6, 34.4] 
cov.sort()
service = ['autoresponder-parent', 'cc-babel-backend', 'cc-bulk-service-backend', 'cc-camunda-optimize-backend', 
           'cc-cert-requester-backend', 'cc-config-library-writer', 'cc-consultation-backend', 'cc-conversation-backend', 
           'cc-decide-cisnet-backend', 'cc-decide-cons-drools-model-backend', 'cc-decide-decision-backend', 
           'cc-decide-decision-drools-model-backend', 'CC-DOCUMENT-MANAGER-BACKEND', 'cc-embedded-configuration-lib', 
           'cc-esif-internal-consultations-backend', 'cc-esif-internal-consultations-drools-model-backend', 
           'cc-external-communication-backend', 'cc-internal-communication-backend', 
           'cc-internal-communication-drools-model-backend', 'cc-internal-communication-reporting-backend', 
           'cc-kafka-oracle-bridge-backend', 'cc-kafka-sse-bridge-backend', 'cc-my-tasks-service-backend', 
           'cc-notification-backend', 'cc-process-pfm-details-backend', 'cc-regio-business-backend', 
           'cc-regio-business-helper-backend', 'cc-reports-backend', 'CC-REPORTS-GENERATOR-BACKEND', 
           'cc-rule-based-task-details', 'cc-rule-based-task-details-backend', 'cc-saga-lib-root', 
           'cc-service-task-ares-backend', 'cc-servicetask-client-backend', 'CC-SFC-BACKOFFICE-BACKEND', 
           'cc-sfc-broker-backend', 'CC-SHAREPOINT-BACKEND', 'cc-signature-backend', 'cc-sync-compass-backend', 
           'cc-ta-cci-creator-backend', 'cc-task-allocation-backend', 'cc-task-details-backend', 
           'cc-taskActions-backend', 'cc-taxonomy-service-backend', 
           'cc-tls-config-lib', 'clock-backend', 'compass-demo-service-backend', 
           'dynamictask-actions-backend', 'flex-builder-service', 'flex-service', 
           'mywp-notifications-middleware', 'portfolio-manager-service', 'process-centre-service', 
           'process-navigator-service', 'springboot-starter-backend', 'task-details-provider-camunda-root', 'user-profile']
service.sort()

new_cov=[55.5555555555556, 95.0819672131148, 25.0, 69.2307692307692, 100.0, 100.0, 53.2663316582915, 0.0, 76.875, 75.0778816199377, 
0.0, 100.0, 30.0, 54.4303797468354, 0.0, 80.0, 0.0, 82.8767123287671, 
0.0, 86.9565217391304, 97.7272727272727, 100.0, 0.0, 0.0, 0.0, 70.8333333333333, 80.0, 100.0, 0.0, 53.7037037037037, 0.0,
 85.4545454545455,  0.0, 44.1791044776119, 51.063829787234,  49.2012779552716,  6.92520775623269] 
new_cov.sort()

service_newcov=['cc-babel-backend', 'cc-camunda-optimize-backend', 'cc-decide-cons-drools-model-backend', 
                'cc-decide-decision-backend', 'CC-DOCUMENT-MANAGER-BACKEND',  'cc-embedded-configuration-lib',  
                'cc-esif-internal-consultations-backend', 'cc-external-communication-backend',
 'cc-internal-communication-backend',  'cc-kafka-sse-bridge-backend',  'cc-my-tasks-service-backend',  
 'cc-notification-backend',  'cc-regio-business-backend',  'cc-reports-backend',  'CC-REPORTS-GENERATOR-BACKEND',
 'cc-rule-based-task-details',  'cc-rule-based-task-details-backend',
 'cc-saga-lib-root',  'cc-service-task-ares-backend',  'cc-servicetask-client-backend',  'CC-SFC-BACKOFFICE-BACKEND', 
 'cc-sfc-broker-backend', 'CC-SHAREPOINT-BACKEND',  'cc-signature-backend',  'cc-sync-compass-backend',  
 'cc-ta-cci-creator-backend',  'cc-task-allocation-backend',  'cc-taskActions-backend',  'cc-tls-config-lib',  
 'clock-backend',  'flex-builder-service',  'flex-service', 'mywp-notifications-middleware',  'portfolio-manager-service',  
 'process-centre-service',  'task-details-provider-camunda-root',  'user-profile']

service_newcov.sort()

service_d = []


# VBP = 0 # compteur des valeurs bien placées
# VMP = 0 # compteur des valeurs mal placées

# for i in range(0, len(service)):
#     if service[i]==service_newcov[i]:
#         print("La valeur", service[i], "de l'indice", i, "est bien placée")
        
#         VBP += 1
#     if service[i] in service_newcov[:i]+service_newcov[i+1:]:
#         print("La valeur", service[i], "de l'indice", i, "est mal placée") 
#         new_cov.append(0.0)  
#         service_newcov.append(service[i])
#         VMP += 1 
 
# print(len(service_newcov), len(new_cov))
# print("Nombre de valeurs bien placées:", VBP)
# print("Nombre de valeurs mal placées:", VMP)


# liste la plus longue: 
# print(len(service),len(cov))    #57 57
# print(len(service_newcov),len(new_cov)) #37 37

for s in service:
    for j in service_newcov:
        if j == s:
            print(j,s)
        else:
            while len(service) > len((service_newcov)): 
                new_cov.append(0.0)
                service_newcov.append(s)
 

print(len(service),len(cov))    #57 57
print(len(service_newcov),len(new_cov)) #57 57
print(service_newcov,new_cov) #57 57
