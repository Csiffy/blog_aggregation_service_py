
# import libraries
import requests
from lxml import etree
from lxml import html

#Necessary
import urllib
from lxml.html import fromstring

url = 'https://wordpress.com/learn-more/?v=blog'
page = requests.get(url, timeout=5)

output = {};
atom_array = [];
rss_array = [];

#if page.status_code == requests.codes.ok:
#  print(page.status_code)
#  print(page.headers['content-type'])
#  print(page.encoding)
#  contentb = page.content
#  contentt = page.text

def create_array(link, type):
  atom_array.append('atom-test')
  atom_array.append('atom-test2')
  atom_array.append('atom-test3')
  rss_array.append('rss-test')
  rss_array.append('rss-test2')
  rss_array.append('rss-test3')
  pass


def return_output():
  output['atom'] = atom_array
  output['rss'] = rss_array
  print(output)
  #console.log(JSON.stringify(output));

print('')
print('')
content = urllib.request.urlopen(url).read().decode('utf-8')
doc = fromstring(content)
#print(doc.find_class('wpcom-landing'))
for child in doc:
  print(child.tag, child.attrib)
iters = doc.getiterator()
for item in iters:
  stag = item.tag
  stype = item.attrib.get('type')
  stitle = item.attrib.get('title')
  shref = item.attrib.get('href')
  sitems = item.items()
  if (stag == "link"):
    print('Tag: ' + str(stag) + ' Title: ' + str(stitle) + ' Type: ' + str(stype) + ' href: ' + str(shref))
create_array('','')

return_output()

  
