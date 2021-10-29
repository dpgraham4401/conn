"""
entry point for starship enterprise
"""
import sys
from pathlib import Path
from conn.conn import run

if not sys.version_info > (2, 7):
    print('error: python version 2 not supported')
    sys.exit(1)


def main():
    """
    conn entry point
    """
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help' or sys.argv[1] =='-h':
            print('not helpful')
        elif Path(sys.argv[1]).is_file():
            run(sys.argv[1])
        else:
            print('config file not found at', sys.argv[1])
            sys.exit(1)

if __name__ == '__main__':
    main()
