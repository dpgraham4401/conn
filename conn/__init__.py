"""
src/__init__.py
entry point for starship enterprise
@author dpgraham4401
"""
import sys
from conn.conn import main
# import os

# sys.path.append(os.path.join(os.path.dirname(__file__), "meta"))

if __name__ == '__main__':
    try:
        # print(sys.path)
        main()
    except KeyboardInterrupt:
        print("\ninterrupted.")
        sys.exit(1)

