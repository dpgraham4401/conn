"""Conn high level functionality"""
import configparser
from pathlib import Path
import sys
import domain


def run(config_path):
    """Initiate conn"""
    print("Conn started: You have the conn")
    read_config(config_path)


def read_config(config_path):
    """read runtime parameters"""
    config = configparser.ConfigParser()
    config.read(config_path)
    # check configurations
    print("checking configs")
    if not Path(config.get('excel', 'path')).is_file():
        print("\tPath exist:", config.get('excel', 'path'))
        sys.exit(1)
