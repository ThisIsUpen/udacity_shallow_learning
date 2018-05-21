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
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#print len(enron_data.values()[0])
#print enron_data

poi_count = 0
for item in enron_data.values():
	if item["poi"] == 1:
		poi_count = poi_count + 1
print "poi count",poi_count

poi_textpath = "../final_project/poi_names.txt"
with open(poi_textpath,"r") as f:
	strings = re.findall(r"\(y\)|\(n\)",f.read())

print len(strings)

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

salary_count = 0
email_count = 0
for item in enron_data.values():
	if item["salary"] != "NaN":
		salary_count += 1
	if item["email_address"] != "NaN":
		email_count +=1
print salary_count, email_count

"""
	number and percentage of people having 'NaN' as total payments
"""
nan_totalpayment_count = 0
for item in enron_data.values():
	if item["total_payments"] == "NaN":
		nan_totalpayment_count += 1

nan_totalpayment_percentage = (float(nan_totalpayment_count)/len(enron_data))*100.0
print nan_totalpayment_count, nan_totalpayment_percentage

"""
	number and percentage of poi having 'NaN' as total payments
"""
poi_nan_totalpayment_count = 0
for item in enron_data.values():
	if item["poi"] == 1 and item["total_payments"] == "NaN":
		poi_nan_totalpayment_count += 1

poi_nan_totalpayment_percentage = (float(poi_nan_totalpayment_count)/len(enron_data))*100.0
print "poi with NaN as total payment",poi_nan_totalpayment_count,poi_nan_totalpayment_percentage

"""
	number and percentage of people having 'NaN' as total payments when 10 poi with NaN total payments added
"""
nan_totalpayment_count_10 = 0
for item in enron_data.values():
	if item["total_payments"] == "NaN":
		nan_totalpayment_count_10 += 1

new_val = nan_totalpayment_count_10+10.0
new_total = len(enron_data)+10.0

nan_totalpayment_percentage_10 = (new_val/new_total)*100.0
print new_val,nan_totalpayment_percentage_10
print new_total

