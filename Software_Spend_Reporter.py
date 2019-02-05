#!/usr/bin/env python

# Author: Mandeep Singh
# Contact: msingh98@uw.edu
# Developed for: ServiceNow
#
# This is the main script that runs the Software_Spend_Reporter.

import sys
import os
from Company import Company
from pandas import read_csv

# The following if else statements stop the execution of the script if
# the path to the file is not provided or if the path to the file is
# invalid
if len(sys.argv) < 2:
    print("Please enter path to file")
    sys.exit()
elif not os.path.exists(sys.argv[1]):
    print("file not found!")
    sys.exit()


# Create a dictionary of product data by companies from the given path
# to the CSV file
#   path_to_csv: path to CSV file entered in the command line
#   returns: returns a dictionary containing company name as key
#            and Company object as value
def create_companies_dictionary(path_to_csv):
    csv_data = read_csv(path_to_csv)
    companies = dict()
    for index, row in csv_data.iterrows():
        vendor = row['Vendor']
        if vendor not in companies.keys():
            company_temp = Company(vendor)
            companies[vendor] = company_temp
        company = companies[vendor]
        company.add_product(row['Product'], row['Amount'])
    return companies


companies_dict = create_companies_dictionary(sys.argv[1])

# Prints the required output by iterating through a sorted list of companies
for company in sorted(companies_dict.keys()):
    companies_dict[company].print_cost()
