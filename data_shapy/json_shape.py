import argparse
import os
import pprint
import json

from data_shapy.data_shape import summarize_data_shape


def main():
    parser = argparse.ArgumentParser(description="Summarizes data shape of contents of a json file.")
    parser.add_argument('json_path', help='path to json file')

    args = parser.parse_args()
    json_path = args.json_path
    if not os.path.exists(json_path):
        parser.error('Could not find {}'.format(json_path))

    try:
        json_data = json.load(open(json_path))
    except json.JSONDecodeError as e:
        parser.error('could not parse contents of {} as json: {}'.format(json_path, e))

    pprint.pprint(summarize_data_shape(json_data))
