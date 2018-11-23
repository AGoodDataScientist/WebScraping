# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:17:34 2018

@author: Baalaji Manivannan
"""

from requests import get
from bs4 import BeautifulSoup
import pandas as pd
urlname = "books_1"
url = u"http://books.toscrape.com/catalogue/category/"+urlname+"/index.html"
response= get(url)
soup = BeautifulSoup(response.text,"html.parser")
tablelist = soup('div',class_="side_categories")[0].ul.li.ul
counter = 0
pageno = 1
for i in tablelist:
    if counter%2 == 0:
        counter += 1
        pageno += 1
        try:
            pagename = i.findNextSibling('li').text.strip().replace(' ','-').lower()
        except:
            break
        urlname = pagename+"_"+str(pageno)
        url = u"http://books.toscrape.com/catalogue/category/books/"+urlname+"/index.html"
        response= get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        bookname = []
        bookprice = []
        instock = []
        sno = []
        snocount = 0
        totalpage = int(int(soup.find("form",class_="form-horizontal").text.strip().split(" ")[0])/20)
        booklist = soup.find('ol',class_="row")
        bname = booklist.find("article",class_="product_pod").h3.a.text
        bprice = booklist.find("div",class_="product_price").find("p",class_="price_color").text
        instockdet = booklist.find("div",class_="product_price").find("p",class_="instock availability").text.strip()
        sno.append(snocount)
        bookname.append(bname)
        bookprice.append(bprice)
        instock.append(instockdet)
        for k in booklist:
            try:
                snocount += 1
                bname = k.findNextSibling("li").find("article",class_="product_pod").h3.a.text
                bprice = k.findNextSibling("li").find("div",class_="product_price").find("p",class_="price_color").text
                instockdet = k.findNextSibling("li").find("div",class_="product_price").find("p",class_="instock availability").text.strip()
                sno.append(snocount)
                bookname.append(bname)
                bookprice.append(bprice)
                instock.append(instockdet)
            except:
                break
        for j in range(2,totalpage+2):
            pagenumber = "page-"+str(j)
            url = u"http://books.toscrape.com/catalogue/category/books/"+urlname+"/"+pagenumber+".html"
            response= get(url)
            soup = BeautifulSoup(response.text,"html.parser")
            booklist = soup.find('ol',class_="row")
            bname = booklist.find("article",class_="product_pod").h3.a.text
            bprice = booklist.find("div",class_="product_price").find("p",class_="price_color").text
            instockdet = booklist.find("div",class_="product_price").find("p",class_="instock availability").text.strip()
            sno.append(snocount)
            bookname.append(bname)
            bookprice.append(bprice)
            instock.append(instockdet)
            for k in booklist:
                try:
                    snocount += 1
                    bname = k.findNextSibling("li").find("article",class_="product_pod").h3.a.text
                    bprice = k.findNextSibling("li").find("div",class_="product_price").find("p",class_="price_color").text
                    instockdet = k.findNextSibling("li").find("div",class_="product_price").find("p",class_="instock availability").text.strip()
                    sno.append(snocount)
                    bookname.append(bname)
                    bookprice.append(bprice)
                    instock.append(instockdet)
                except:
                    break
        booklist_df = pd.DataFrame({'S.No':sno,'Book Name':bookname,'Book Price':bookprice,'Instock detail':instock})
        booklist_df.to_csv("D:\MyWorks\PythonLanguage\WebScraping\CSV\\"+urlname+".csv")
    else:
        counter += 1