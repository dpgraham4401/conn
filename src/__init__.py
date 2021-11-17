"""
entry point for starship enterprise
"""
import sys
import argparse

def main():
    """
    Parse command line arguemtns and start
    """
    parser = argparse.ArgumentParser(description="CLI automation goodness for e-Manifest task")
    parser.add_argument('verb',
                        help='path to the file',
                        choices=['meta', 'test' ],)
    parser.add_argument('--display', '-d',
                        help='Display parsed info',
                        choices=['contacts', 'stats' ],
                        action='store')
    args = parser.parse_args()
    
    # test
    if args.verb == "meta":
        print("meta")
    elif args.verb == "test":
        print("test!")
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted.")
        sys.exit(1)
