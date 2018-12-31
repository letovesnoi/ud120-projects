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

# person_of_interest = 0

# How many folks in this dataset have a quantified salary? What about a known email address?
# quantified_salary = 0
# email_address = 0
nan_total_payments = 0
percent_nan_total_payments = 0
for lastname_firstname_middleinitial in enron_data:
#     print lastname_firstname_middleinitial
#     if enron_data[lastname_firstname_middleinitial]["poi"] == 1:
#         person_of_interest += 1
#     if enron_data[lastname_firstname_middleinitial]['salary'] != 'NaN':
#         quantified_salary += 1
#     if enron_data[lastname_firstname_middleinitial]['email_address'] != 'NaN':
#         email_address += 1
    if enron_data[lastname_firstname_middleinitial]['total_payments'] == 'NaN':
        nan_total_payments += 1
# print 'Quantified salary: ', quantified_salary
# print 'Known email address: ', email_address
total = len(enron_data)
percent_nan_total_payments = int(nan_total_payments * 1.0 / total * 100)
print 'NaN for their total payments:', nan_total_payments, ' percentage:', percent_nan_total_payments, '%'

# print enron_data['PRENTICE JAMES']['total_stock_value']
# print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
# print enron_data['SKILLING JEFFREY K']['exercised_stock_options']


# CEO of Enron: Jeffrey Skilling
# Chairman of the Enron board of directors: Kenneth Lay
# CFO (chief financial officer) of Enron: Andrew Fastow
# Who took home the most money?
# money_lay = enron_data['LAY KENNETH L']['total_payments']
# money_skilling = enron_data['SKILLING JEFFREY K']['total_payments']
# money_fastow = enron_data['FASTOW ANDREW S']['total_payments']
# most_money = max(money_lay, money_skilling, money_fastow)
# print 'Lay money: ', money_lay, '\nSkilling money: ', money_skilling, '\nFastow money: ', money_fastow
# print '\nMost money: ', most_money
