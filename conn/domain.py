"""
Email domain name matching for generator registration
"""
from numpy import fromstring
import pandas as pd

TEST_PATH = "./test_sites.xlsx"


def read_raw_data(data_file_path):
    """ read site info from excel/csv file"""
    if data_file_path[-3:] == "csv":
        raw_data = pd.read_csv(data_file_path, keep_default_na=False, na_values=[''])
    elif data_file_path[-4:] == "xlsx" or data_file_path[-5:-1] == "xlsm":
        raw_data = pd.read_excel(data_file_path, keep_default_na=False)
    # ToDo: add exception for non csv/xlsx files
    return raw_data

def get_domains(raw_data):
    """get a unique list of email domains from the raw data"""
    raw_emails = raw_data["Contact email"].unique()
    domains = [None] * len(raw_emails)
    for i in range(0, len(raw_emails)):
        # print(raw_emails[i])
        if "@" in raw_emails[i]:
            domains[i] = raw_emails[i].split('@')[1]
    domains = set(domains)
    return domains
    

# Testing area
data = read_raw_data(TEST_PATH)
id_data = get_domains(data)
for i in id_data:
    print(i)
