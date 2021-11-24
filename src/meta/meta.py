"""
src/meta.py
high level functionality related to pulling data from https://rcraquery.epa.gov
@author: dpgraham4401
"""

from src.meta.auth import token
from src.meta.query import query
from src.meta.query import save_output


def run_meta(args):
    """Meta subcommand decision tree"""
    if args.auth:
        token()
    elif args.query:
        token()
        res = query(args.query, args.output)
        if res.status_code == 200:
            if args.output:
                print("Saving data")
                save_output(res, args.output)
