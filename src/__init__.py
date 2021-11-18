"""
entry point for starship enterprise
"""
import sys
import argparse
from src.meta.meta import run_meta

def main():
    """
    Parse command line argument and start
    """
    parser = argparse.ArgumentParser(description="CLI automation goodness for e-Manifest tasks")

    parser.add_argument('-v','--version', help='Display version number and quit')

    # breakdown the functionality in subcommands 
    subparsers = parser.add_subparsers(dest='sub_cmd', help='conn provides the below subcommands')

    parser_meta = subparsers.add_parser('meta', help='Pull data from Metabase, defaults to authorize')
    parser_meta.add_argument('--query', 
                            help='Pull query results from metabase')
    parser_meta.add_argument('--auth', 
                            action='store_true',
                            help='authorize your metabase account')
    # parser_meta.add_argument('--card',
    #                         # dest='meta_cmd',
    #                         help='query number to pull')

    parser_meta = subparsers.add_parser('excel', help='Work with excel and cvs')
    parser_meta.add_argument('read', help='Pull query results from metabase')
    parser_meta.add_argument('--sheet', help='query number to pull')

    args = parser.parse_args()

    if args.version:
        print("placeholder")
    if args.sub_cmd == "meta":
        run_meta(args)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted.")
        sys.exit(1)

