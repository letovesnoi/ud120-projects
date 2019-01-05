#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0)

# Two people made bonuses of at least 5 million dollars,
# and a salary of over 1 million dollars
like_bandits = {name for name, dict_value in data_dict.items() if (dict_value['bonus'] > 5000000 and dict_value['salary'] > 1000000 and dict_value['bonus'] != 'NaN' and dict_value['salary'] != 'NaN')}
print like_bandits

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


