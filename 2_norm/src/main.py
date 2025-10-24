import logging
import yaml
import os

def main():
    config = get_config()

    logging.basicConfig(
        level=config['logging']['level'],
        format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename = os.path.join(config['paths']['log_dir'], config['logging']['file'])
    )
    logging.info("Hello, World!")

def get_config():
    config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), \
                                '..', 'config', 'default.yaml')

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        return config

if __name__ == '__main__':
    main()