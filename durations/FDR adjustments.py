from durations.duration_analysis import import_data
from durations.duration_analysis import durations_feature
import operator

ALPHA = 0.05

features = [
    'bac',
    'cry',
    'fil',
    'lau',
    'len',
    'ove',
    'sil'
]

pvalues = {}

control_data, depressed_data = import_data()

for feature in features:
    try:
        pvalue = durations_feature(feature, control_data, depressed_data)[1]
    except TypeError:
        continue
    pvalues[feature] = pvalue

pvalues = {feature: pvalues[feature] for feature in pvalues.keys() if pvalues[feature] < ALPHA}
sorted_pvalues = sorted(pvalues.items(), key=operator.itemgetter(1))
test_count = len(features)

thresholds = {}

for i in range(len(pvalues)):
    threshold = ALPHA * ((i+1) / test_count)
    thresholds[sorted_pvalues[i][0]] = threshold

for feature, pvalue in sorted_pvalues:
    print('{0} {1} -- threshold: {2}'.format(feature, pvalue, thresholds[feature]))
