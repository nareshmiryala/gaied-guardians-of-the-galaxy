import json
import os

def load_config(config_file):
    config_path = os.path.join(os.path.dirname(__file__), '..', config_file)
    with open(config_path, "r") as file:
        return json.load(file)

# Load the configuration
CONFIG = load_config("config.json")