"""
entry point for starship enterprise
"""
import sys
import configparser

if not sys.version_info > (2, 7):
    print('error: python version 2 not supported')
    sys.exit(1)


def main():
    """
    conn entry point
    """
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help' or sys.argv[1] =='-h':
            print('yoohoo')
        else:
            print('unknown argument: "' + sys.argv[1] + '"')

if __name__ == '__main__':
    main()
