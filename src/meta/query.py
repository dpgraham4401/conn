"""
src/query.py
pulling data from https://rcraquery.epa.gov
@author: dpgraham4401
"""

import os
import requests

BASE_URL = 'https://rcraquery.epa.gov/metabase'

def get_cards(card_type):
    """Request query (card) options"""
    auth_url = BASE_URL + '/api/card'
    token_id = os.getenv('META_TOKEN')
    meta_head = {'Content-Type': 'application/json',
                 'X-Metabase-Session': token_id,
                 'f': card_type}
    res = requests.get(auth_url, headers=meta_head)
    res = res.json()
    return res


def query(card_id, export_frmt):
    """GET metabase card"""
    auth_url = BASE_URL + '/api/card/' + card_id + '/query/' + export_frmt
    print(auth_url)
    token_id = os.getenv('META_TOKEN')
    meta_head = {'Content-Type': 'application/json',
                 'X-Metabase-Session': token_id}
    res = requests.post(auth_url, headers=meta_head)
    res = res.json()
    return res
