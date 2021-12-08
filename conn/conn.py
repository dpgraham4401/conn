"""
conn/conn.py
The warp drive (conn's high level functionality and CLI)
@author: dpgraham4401
"""

import argparse
import sys
from conn.email.outlook import run_who
from conn.meta.meta import run_meta

# Todo: automatically update version
__version__ = '0.0.1'


def main():
    """
    The starting point
    """
    args = conn_cli()

    if args.sub_cmd == "meta":
        run_meta(args)
    elif args.sub_cmd == "who":
        run_who(args)


def conn_cli():
    """ Conn's command line interface for conn """
    # Top level: --version, --help, sub commands
    parser = argparse.ArgumentParser(description="CLI automation goodness for e-Manifest tasks")
    parser.add_argument('-v','--version', action='version', version="%(prog)s "+__version__+"")
    
    subparsers = parser.add_subparsers(dest='sub_cmd', help='conn provides the below subcommands')

    # Conn subcomands (meta, excel, email)
    parser_meta = subparsers.add_parser('meta', help='Pull data from Metabase, defaults to authorize')
    parser_excel = subparsers.add_parser('excel', help='Work with excel and cvs')
    parser_email = subparsers.add_parser('email', help='send emails')
    if "who" in sys.argv:
        parser_conn = subparsers.add_parser('who', help='who has the conn?')
    # Todo: subcommand utilities for email, RCRAInfo API

    # Meta subcommands and options
    group_meta = parser_meta.add_mutually_exclusive_group()
    group_meta.add_argument('-a','--auth', 
                            action='store_true',
                            help='authorize your metabase account')
    group_meta.add_argument('-q','--query',
                            action='store',
                            help='metabase query number to pull results from')
    parser_meta.add_argument('-p','--parameter', 
                            action='store',
                            help='parameter for query')
    parser_meta.add_argument('-o', '--output',
                            default='./conn_output.json',
                            action='store',
                            help='specify .csv or .json output, defaults to "./conn_output.json"')

    # Excel subcommands and options
    parser_excel.add_argument('-read', help='read data into pandas dataframe')
    parser_excel.add_argument('-sheet', help='sheet name or number (zero indexed)')
    
    # Email subcommands and options
    parser_email.add_argument('--test', help='test emaail and pywin32')
    parser_conn.add_argument('-u', help='who has the conn')

    args = parser.parse_args()
    return args
