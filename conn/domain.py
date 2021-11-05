"""
Email domain name matching for generator registration
"""
import pandas as pd


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


def group_contacts(domains, raw_data):
    con_email = raw_data["Contact email"]
    user_emails = raw_data["Site Manager Emails"]
    # loop through unique email domains
    for dom in domains:
        num_sites = 0
        num_manifest = 0
        site_list = ""
        # find contact emails with that same domain name
        for i in range(0, len(con_email)):
            con_split = con_email[i].split('@')
            if len(con_split) > 1:
                if dom == con_split[1] and raw_data["Site Manager"][i] == "N":
                    num_sites += 1
                    site_list = site_list + raw_data["Generator Site ID"][i] \
                        + "; "
            # if len(user_emails[i].split("@") > 1):
                # ToDo: if user emails matches domain, but contact not present
        print(dom, ":", num_sites)
        print(site_list)

    

# Testing area
TEST_PATH = "./test_sites.xlsx"

data = read_raw_data(TEST_PATH)
domains_test = get_domains(data)
group_contacts(domains_test, data)
# for i in id_data:
    # print(i)
