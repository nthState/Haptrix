import os
import json
from collections import namedtuple
import re
from jinja2 import Template
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-t", "--template", dest="template", help="template file")
parser.add_argument("-src", "--source", dest="source", help="source directory")
parser.add_argument("-dst", "--destination", dest="destination", help="destination directory")

args = parser.parse_args()


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
    
def replaceIfPrefix(document, prefixKey, str):
    if 'prefixes' in document:
        if prefixKey in document['prefixes']:
            prefix =  document['prefixes'][prefixKey]
            return "{}/{}".format(prefix,str)
    return str

# def customDocumentationDecoder(dic):
#     return namedtuple('Documentation', dic.keys())(*dic.values())

templateFile = args.template
jsonDirectory = args.source
targetDirectory = args.destination

# Read in template

with open (templateFile, "r") as file:
    templateStr=file.read()

# Read in JSON files

json_files = [pos_json for pos_json in os.listdir(jsonDirectory) if pos_json.endswith('.json')]

# Load all objects into a filename.json:object dictionary
objectDic = {}
for index, js in enumerate(json_files):
    with open(os.path.join(jsonDirectory, js)) as json_file:
        key = os.path.basename(os.path.normpath(js))
        print("Loading file {} {}".format(js, key))
        objectDic[key] = json.load(json_file)

for index, js in enumerate(json_files):
    print("Pricessing file {}".format(js))
    
    newFile = []
    
    with open(os.path.join(jsonDirectory, js)) as json_file:
        documentation = json.load(json_file)
        
        t = Template(templateStr)
        
        # replace links in sections
        sections = documentation['sections']
        for section in sections:
            if 'link' in section and section['link'] != "":
                print("Replacing: {}".format(section['link']))
                print("With: {}".format(objectDic[section['link']]['urls']['githubDocs']))
                section['link'] = replaceIfPrefix(documentation, 'githubDocs', objectDic[section['link']]['urls']['githubDocs'])
                
        # Replace image paths in sections
        for section in sections:
            if 'image' in section and section['image'] != "":
                print("Replacing: {}".format(section['image']))
                section['image'] = section['image']
                
        # Replace body image
        if 'bodyImage' in documentation:
            documentation['bodyImage'] = documentation['bodyImage']
                
        # replace links in breadcrumbs
        newCrumbs = []
        if 'breadcrumbs' in documentation:
            breadcrumbs = documentation['breadcrumbs']
            for crumb in breadcrumbs:
                link = objectDic[crumb]['urls']['githubDocs']
                linkText = os.path.basename(os.path.normpath(link))
                link = replaceIfPrefix(documentation, 'githubDocs', link)
                x = {
                    "link": link,
                    "linkText": linkText
                }
                newCrumbs.append(x)
        
        dic = {
            "title": documentation['title'],
            "body": documentation['body'],
            "metadata": documentation['metadata'],
            "bodyImage": (documentation['bodyImage'] if 'bodyImage' in documentation else None),
            "sections": sections,
            "breadcrumbs": newCrumbs,
            "helpBookAnchor": documentation['helpBookAnchor']
        }
        
        print("dic {}".format(dic))
        
        result = t.render(dic)
    
    newFileName = documentation['urls']['githubDocs']
    filePath = os.path.join(targetDirectory, newFileName)
    os.makedirs(os.path.dirname(filePath), exist_ok=True)
    with open(filePath, "w") as md_file:
        md_file.write(result)
    