from counts.count_analysis import import_data
from counts.count_analysis import count_feature

control_data, depressed_data, control_duration, depressed_duration = import_data()
chisquare = count_feature('cry', control_data, depressed_data, control_duration, depressed_duration)

print(chisquare)
