# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:49:23 2018

@author: Baalaaji Manivannan
"""

from requests import get
from bs4 import BeautifulSoup
url = u"https://www.imdb.com/search/title?title_type=feature&year=2007-01-01,2007-12-31&start=1&ref_=adv_nxt"
response = get(url)
soup = BeautifulSoup(response.text,"html.parser")
limit = int(soup.find("div",{'class':'desc'}).span.text.split(' ')[2].replace(',',''))
orderno = []
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
startval = 1
counter = 0
limit = round(limit/50)
for lp in range(limit):
    url = u"https://www.imdb.com/search/title?title_type=feature&year=2007-01-01,2007-12-31&start="+str(startval)+"&ref_=adv_nxt"
    response = get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    for i in soup.find_all("div",class_="lister-item mode-advanced"):
        try:
            orderno.append(i.find('div',class_="lister-item-content").h3.find("span",class_="lister-item-index unbold text-primary").text.replace(',','').replace('.',''))
        except:
            orderno.append("No Movie Rank specified")
        try:
            names.append(i.find('div',class_="lister-item-content").h3.a.text)
        except:
            names.append("No Movie Name specified")
        try:
            years.append(i.find('div',class_="lister-item-content").h3.find("span",class_="lister-item-year text-muted unbold").text.replace('(','').replace(')',''))
        except:
            years.append("No Released Year specified")
        try:
            imdb_ratings.append(i.find('div',class_="lister-item-content").div.div.strong.text)
        except:
            imdb_ratings.append("No IMDB Rating")
        try:
            metascores.append(i.find('div',class_="lister-item-content").div.find("div",class_="inline-block ratings-metascore").span.text)
        except:
            metascores.append("No MetaScore")
        try:
            votes.append(i.find('div',class_="lister-item-content").find("p",attrs={'class':'sort-num_votes-visible'}).find("span",attrs = {'name':'nv'}).text)
        except:
            votes.append("No Votes")
    startval += len(soup.find_all("div",class_="lister-item mode-advanced"))

import pandas as pd
test_df = pd.DataFrame({'S.No':orderno,'Movie Name':names,'Released Year':years,'IMDB Rating':imdb_ratings,'Metascores':metascores,'Votes':votes})
test_df.loc[:,'Released Year'] = test_df['Released Year'].astype(str).str[-4:].astype(int)
test_df.loc[:,'IMDB Rating'] = test_df['IMDB Rating'].astype(float)*10
test_df.to_csv(u'D:\MyWorks\PythonLanguage\WebScraping\Movielist.csv')