#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("final_project_dataset.pkl", "r"))

print len(enron_data)
print len(enron_data["METTS MARK"])


filtered_dict = {k: v for k, v in enron_data.iteritems() if v["poi"]==1}
print len(filtered_dict)
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


with open('poi_names.txt') as f:
    lines = f.read().splitlines()

print len(lines)

count=0;
for line in lines:
    name = line[4:].upper()
    print name
    if(name in enron_data):
        count=count+1;



print count;

print enron_data["PRENTICE JAMES"]["total_stock_value"]

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]

counter=0;
for k,v in enron_data.iteritems():
    if (v["total_payments"]=="NaN"):
        counter=counter+1;

print counter;