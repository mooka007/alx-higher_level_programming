#!/usr/bin/python3
# Author - MoOka
"""object from json file"""

import json


def load_from_json_file(filename):
    """creates an obj from json file"""
    with open(filename, 'r', encoding="UTF8") as f:
        return (json.load(f))
