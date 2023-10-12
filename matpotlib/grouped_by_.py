import matplotlib.pyplot as plt
import numpy as np


# new_coverage 30
odict_values= ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.67045454545455, 8.44594594594595, 25.0, 27.0408163265306, 30.0, 37.7643504531722, 51.063829787234, 51.3888888888889, 55.5555555555556, 57.1428571428571, 69.2307692307692, 70.8333333333333, 75.0778816199377, 76.875, 80.0, 82.8767123287671, 86.9565217391304, 92.8571428571429, 95.0819672131148, 100.0, 100.0, 100.0, 100.0])
odict_keys = (['cc-external-communication-backend', 'cc-rule-based-task-details-backend', 'cc-service-task-ares-backend', 'cc-signature-backend', 'cc-sync-compass-backend', 'cc-tls-config-lib', 'mywp-notifications-middleware', 'flex-builder-service', 'user-profile', 'cc-decide-cons-drools-model-backend', 'task-details-provider-camunda-root', 'cc-regio-business-backend', 'portfolio-manager-service', 'process-centre-service', 'cc-reports-backend', 'cc-babel-backend', 'cc-task-details-backend', 'cc-decide-decision-backend', 'cc-ta-cci-creator-backend', 'cc-kafka-sse-bridge-backend', 'cc-internal-communication-backend', 'cc-rule-based-task-details', 'cc-saga-lib-root', 'cc-servicetask-client-backend', 'flex-service', 'cc-camunda-optimize-backend', 'cc-embedded-configuration-lib', 'cc-notification-backend', 'cc-task-allocation-backend', 'cc-taskActions-backend'])

# new_line_coverage 30
line_coverage_values= ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.03571428571429, 12.6315789473684, 25.0, 26.8817204301075, 30.0, 41.7391304347826, 49.2307692307692, 55.5555555555556, 57.1428571428571, 64.2857142857143, 65.0, 78.1818181818182, 80.0, 80.1587301587302, 87.5, 88.2352941176471, 98.0392156862745, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_coverage_keys=(['cc-external-communication-backend', 'cc-rule-based-task-details-backend', 'cc-service-task-ares-backend', 'cc-signature-backend', 'cc-sync-compass-backend', 'cc-tls-config-lib', 'mywp-notifications-middleware', 'user-profile', 'flex-builder-service', 'cc-decide-cons-drools-model-backend', 'task-details-provider-camunda-root', 'cc-regio-business-backend', 'portfolio-manager-service', 'cc-reports-backend', 'process-centre-service', 'cc-task-details-backend', 'cc-babel-backend', 'cc-decide-decision-backend', 'cc-kafka-sse-bridge-backend', 'cc-rule-based-task-details', 'cc-internal-communication-backend', 'cc-servicetask-client-backend', 'cc-saga-lib-root', 'cc-camunda-optimize-backend', 'cc-embedded-configuration-lib', 'cc-notification-backend', 'cc-ta-cci-creator-backend', 'cc-task-allocation-backend', 'cc-taskActions-backend', 'flex-service'])

plt.bar(odict_keys, odict_values, bottom=line_coverage_values)
plt.bar(odict_keys, line_coverage_values)
plt.xlabel("components")
plt.ylabel("new_coverage")
plt.show()
