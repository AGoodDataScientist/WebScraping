# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:14:19 2018

@author: BGM
"""

import urllib.request
from bs4 import BeautifulSoup
wiki = u"https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page,'html.parser')
#print(soup.find_all("a")[4]["title"])
for link in soup.find_all("a"):
    if link.string != None:
        a = 5
        #print(link.string)

#print(list(soup.children[0]))
for des in soup.descendants:
    print(des.string)
#print(type(link))
