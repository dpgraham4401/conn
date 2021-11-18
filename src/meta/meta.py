"""
src/meta.py
high level functionality related to pulling data from https://rcraquery.epa.gov
@author: dpgraham4401
"""

from src.meta.auth import token

def run_meta(args):
    if args.auth:
        token()
    elif args.query:
        query()