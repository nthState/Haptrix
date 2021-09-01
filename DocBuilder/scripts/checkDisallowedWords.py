import os
import json
from collections import namedtuple
import pathlib
import datetime
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-src", "--source", dest="source", help="source directory")

args = parser.parse_args()


directory = args.source


# Read in JSON files

json_files = [pos_json for pos_json in os.listdir(directory) if pos_json.endswith('.json')]

disallowedWords = [
                "obviously", "obvious",
                "simply", "simple",
                "easily",
                "he",
                "she",
                "blacklist",
                "whitelist",
                "master",
                "slave"
                ]

def check_words(stringToCheck, disallowedWords):
    stringArray = stringToCheck.split(" ")
    for string in stringArray:
        if string.lower() in disallowedWords:
            return True
    return False

for index, js in enumerate(json_files):
    print("Processing file {}".format(js))
    
    fullPath = os.path.join(directory, js)
    
    fname = pathlib.Path(fullPath)
    mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime)

    
    with open(fullPath) as json_file:
        documentation = json.load(json_file)

        dic = {
            "title": documentation['title'],
            "body": documentation['body'],
            "metadata": " ".join(documentation['metadata']),
            "sectionTitles": " ".join(e.get("title", "") for e in documentation['sections']),
            "sectionText": " ".join(e.get("text", "") for e in documentation['sections']),
            "sectionLink": " ".join(e.get("link", "") for e in documentation['sections'])
        }
        
        for value in dic.values():
            if check_words(value, disallowedWords):
                print("Disallowed word found in: {}".format(value))
                exit(1)