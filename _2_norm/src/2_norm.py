import logging
import yaml
import os
from pathlib import Path
import argparse


def main():
    # config = get_config()

    parser = argparse.ArgumentParser(
        prog="merge",
        description="merges a csv & excel file into single file"
    )
    parser.add_argument(
        'input', help="path to folder containing data files")
    parser.add_argument("-v", "--verbose",
                        help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    p = Path(args.input)
    csv_list = p.glob('**/*.csv')
    


    xls_list = p.glob('**/*.xlsx')

    # logging.basicConfig(
    #     level=config['logging']['level'],
    #     format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    #     filename = os.path.join(config['paths']['log_dir'], config['logging']['file'])
    # )
    # logging.info("Hello, World!")




def get_config():
    config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               '..', 'config', 'default.yaml')

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        return config


if __name__ == '__main__':
    main()
