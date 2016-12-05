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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0

for key in enron_data:
    if enron_data[key]["poi"] == 1:
        count+=1

print "Number of POIs in final_project_dataset.pkl: %s" % count

poi_names = open("../final_project/poi_names.txt").readlines()
del poi_names[0:2]
poi_names = [x.strip('\n') for x in poi_names]
print "Number of POIs in poi_names.txt: %s" % len(poi_names)

print "Total stock value owned by James Prentice: %s" % enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Total emails from Wesley Colwell to POIs: %s" % enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Stock options exercised by Jeffrey K Skilling: %s" % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]