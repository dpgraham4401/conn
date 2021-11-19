"""
src/__init__.py
entry point for starship enterprise
@author dpgraham4401
"""
import sys
from src.conn import main

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted.")
        sys.exit(1)

