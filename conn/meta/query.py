"""
conn/query.py
pulling data from https://rcraquery.epa.gov
@author: dpgraham4401
"""

import os
import sys
import requests
import json

BASE_URL = 'https://rcraquery.epa.gov/metabase'


def get_export_fmt(output_path):
    if 'csv' in output_path:
        return 'csv'
    elif 'json' in output_path:
        return 'json'
    else:
        print("ERROR: expected file type .json or .csv, recieved -->", output_path)
        sys.exit(1)


def save_output(result, output_path):
    """write to file"""
    out_format = get_export_fmt(output_path)
    if out_format == "json":
        result = result.json()
        with open(output_path, "w") as f:
            json.dump(result, f)
    elif out_format == "csv":
        with open(output_path, "w") as csvfile:
            csvfile.write(result.text)


def set_query_headers():
    token_id = os.getenv("META_TOKEN")
    meta_head = {'Content-Type': 'application/json',
                 'X-Metabase-Session': token_id}
    return meta_head


def parse_params(args):
    """convert CLI parameters to payload"""
    # template parameters to pass to requests
    # params = {"ignore_cache":True,
    #     "parameters":[{
    #         "type":"category",
    #         "target":["variable",["template-tag","id_var"]],
    #         "value":"ILD021160189"}]}
    if isinstance(args.parameter, str):
        metabase_var = args.parameter.split('=')
    params = {
        'ignore_cache':True,
    }
    params['parameters'] = [{
            "type":"category",
            "target":["variable",["template-tag",metabase_var[0]]],
            "value":metabase_var[1]}]
    params = json.dumps(params)
    return params


def query(args):
    """GET metabase card"""
    card_id = args.query
    output_path = args.output
    meta_head = set_query_headers()
    out_format = get_export_fmt(output_path)
    if args.parameter:
        params = parse_params(args)
        query_url = BASE_URL + "/api/card/" + card_id + "/query"
        res = requests.post(query_url, data=params, headers=meta_head)
    else:
        query_url = BASE_URL + "/api/card/" + card_id + "/query/" + out_format
        res = requests.post(query_url, headers=meta_head)
    return res
