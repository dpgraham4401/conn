"""
src/meta.py
high level functionality related to pulling data from https://rcraquery.epa.gov
@author: dpgraham4401
"""

from src.meta.auth import token
from src.meta.query import query
import json

def run_meta(args):
    """Metabase related logic"""
    if args.auth:
        token()
    elif args.query:
        token()
        res = query(args.query, args.format)
        for i in res:
            print(i)

