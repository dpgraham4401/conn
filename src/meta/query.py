"""
src/query.py
pulling data from https://rcraquery.epa.gov
@author: dpgraham4401
"""

import os
import sys
import requests
import json
import csv
import ast

BASE_URL = 'https://rcraquery.epa.gov/metabase'

# def get_cards(card_type):
#     """Request query (card) options"""
#     auth_url = BASE_URL + '/api/card'
#     token_id = os.getenv('META_TOKEN')
#     meta_head = {'Content-Type': 'application/json',
#                  'X-Metabase-Session': token_id,
#                  'f': card_type}
#     res = requests.get(auth_url, headers=meta_head)
#     res = res.json()
#     return res


def get_export_fmt(output_path):
    if 'csv' in output_path:
        return 'csv'
    elif 'json' in output_path:
        return 'json'
    else:
        print("ERROR: expected file type .json or .csv, recieved -->", output_path)
        sys.exit(1)


def save_output(result, output_path):
    out_format = get_export_fmt(output_path)
    if out_format == "json":
        result = result.json()
        with open(output_path, "w") as f:
            json.dump(result, f)
    elif out_format == "csv":
        with open(output_path, "w") as csvfile:
            csvfile.write(result.text)
    

def query(card_id, output_path):
    """GET metabase card"""
    out_format = get_export_fmt(output_path)
    query_url = BASE_URL + "/api/card/" + card_id + "/query/" + out_format
    token_id = os.getenv("META_TOKEN")
    meta_head = {'Content-Type': 'application/json',
                 'X-Metabase-Session': token_id}
    res = requests.post(query_url, headers=meta_head)
    return res
