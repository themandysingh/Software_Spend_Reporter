#!/usr/bin/env python
import sys
import os
from Company import Company
from pandas import read_csv

if len(sys.argv) < 2:
    print("Please enter path to file")
    sys.exit()
elif not os.path.exists(sys.argv[1]):
    print("file not found!")
    sys.exit()

csv_data = read_csv(sys.argv[1])
companies = dict()
for index, row in csv_data.iterrows():
    vendor = row['Vendor']
    if vendor not in companies.keys():
        company = Company(vendor)
        company.add_product(row['Product'], row['Amount'])
        companies[vendor] = company
    else:
        company = companies[vendor]
        company.add_product(row['Product'], row['Amount'])

for company in sorted(companies.keys()):
    companies[company].print_cost()
