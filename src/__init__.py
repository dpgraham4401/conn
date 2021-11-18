"""
entry point for starship enterprise
"""
import sys
import argparse

def main():
    """
    Parse command line argument and start
    """
    parser = argparse.ArgumentParser(description="CLI automation goodness for e-Manifest task")

    parser.add_argument('-v','--version', help='Display version number and quit')

    # breakdown the functionality in subcommands 
    subparsers = parser.add_subparsers(dest='sub_cmd', help='conn provides the below subcommands')

    parser_meta = subparsers.add_parser('meta', help='Pull data from Metabase')
    parser_meta.add_argument('query', help='Pull query results from metabase')
    parser_meta.add_argument('--card', help='query number to pull')

    parser_meta = subparsers.add_parser('excel', help='Work with excel and cvs')
    parser_meta.add_argument('read', help='Pull query results from metabase')
    parser_meta.add_argument('--sheet', help='query number to pull')

    args = parser.parse_args()
    

    if args.sub_cmd:
        print("meta!")
    if args.query:
        print("  |")
        print("  __query!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted.")
        sys.exit(1)

