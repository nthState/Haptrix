import os
import json
from collections import namedtuple
import pathlib
import datetime
from jinja2 import Template
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-t", "--template", dest="template", help="template file")
parser.add_argument("-src", "--source", dest="source", help="source directory")
parser.add_argument("-dst", "--destination", dest="destination", help="destination directory")

args = parser.parse_args()


def customDocumentationDecoder(dic):
    return namedtuple('Documentation', dic.keys())(*dic.values())

templateFile = args.template
directory = args.source
targetDirectory = args.destination
newFileName = "sitemap.xml"

# Read in template

with open (templateFile, "r") as file:
    templateStr=file.read()

# Read in JSON files

json_files = [pos_json for pos_json in os.listdir(directory) if pos_json.endswith('.json')]

dics = []

for index, js in enumerate(json_files):
    print("Pricessing file {}".format(js))
    
    fullPath = os.path.join(directory, js)
    
    fname = pathlib.Path(fullPath)
    mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime)

    
    with open(fullPath) as json_file:
        #json_text = json.load(json_file)
        documentation = json.load(json_file, object_hook=customDocumentationDecoder)

        dic = {
            "title": documentation.title,
            "url": documentation.urls.githubDocs,
            "lastModificationDate": mtime.strftime('%Y-%m-%d')
        }
        
        dics.append(dic)

# Render
t = Template(templateStr)
result = t.render({"files": dics})

# Write
with open(os.path.join(targetDirectory, newFileName), "w") as md_file:
    md_file.write(result)
    