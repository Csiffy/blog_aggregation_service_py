#!/usr/bin/python3
# -*- coding: utf-8 -*-

__copyright__ = """
    Apache 2.0
    """
__version__ = '0.4.0'
__doc__ = 'for example: python service.py -u https://wordpress.com/learn-more/?v=blog'


# import necessary libraries
import requests
import urllib
import json
import argparse
from lxml import etree
from lxml import html
from lxml.html import fromstring

output = {}
atom_array = []
rss_array = []

def create_array(link, type):
  if (type == "application/rss+xml"):
      rss_array.append(link)
  elif (type == "application/atom+xml"):
      atom_array.append(link)

def return_output():
  output['atom'] = atom_array
  output['rss'] = rss_array
  print(json.dumps(output, separators=(',',':')))

def main():
    parser = argparse.ArgumentParser(description='Query the RSS and ATOM feeds from an URL')
    parser.add_argument('-u','--url', help='Please provide an URL', required=True)
    parsed_args = parser.parse_args()
    url = parsed_args.url
    content = urllib.request.urlopen(url).read().decode('utf-8')
    doc = fromstring(content)
    iters = doc.getiterator()
    for item in iters:
      stag = item.tag
      stype = item.attrib.get('type')
      shref = item.attrib.get('href')
      if (stag == "link" and stype == "application/rss+xml") or (stag == "link" and stype == "application/atom+xml"):
        create_array(shref,stype)
    return_output()

if __name__ == '__main__':
  try:
    main()
  except:
    print("Something went wrong, handle the error")

