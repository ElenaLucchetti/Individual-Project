from durations.duration_analysis import import_data
from durations.duration_analysis import durations_feature

control_data, depressed_data = import_data()
stud_t = durations_feature('lau', control_data, depressed_data)

if not stud_t:
    print("Analysis not run due to lack of feature instances")
else:
    print(stud_t)
