# -*- coding: utf-8 -*-
"""
Created on Thu May 26 09:46:31 2016

        link_detail='\''+'https://lenta.ru' + str(result)+'\''
        print text_news 
        name_news = [child.strip() if isinstance(child, str) else str(child) for child in soup.find('h1', attrs={'class': 'b-text clearfix'})]
        name_news = ''.join(name_news)
        clear_text_detal=''.join(BeautifulSoup(name_news).findAll(text=True))
        name_news = soup.find('h1', 'b-topic__title')
        name_news = ''.join(name_news)
@author: user 
list_word=clear_text_detal.split(' ')
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import pymorphy2
from nltk import FreqDist
#from collections import Counter
import nltk.tokenize
import xlwt, xlrd
from stop_words import get_stop_words
import datetime




#now_date = datetime.date.today()
now_date = datetime.date(2008, 1, 1)
delta = datetime.timedelta(days=1)
year1=now_date.year
month1=now_date.month
day1=now_date.day
i=0
j=0
#stop_words = get_stop_words('russian')
#tknzr = TweetTokenizer()#Для разбития на токены
finish_word = []
n_word = []
text_one_day = ''
morph = pymorphy2.MorphAnalyzer() 
      

t=0
w=0
cv=0
while i<2:
#    if i==0:
#        wb = xlwt.Workbook()
#        ws = wb.add_sheet('A Test Sheet')
#    else:
#        wb = xlrd.open_workbook('D:\\test.xls',formatting_info=True)
#        ws = wb.sheet_by_index(0)
    
    
    year1=now_date.year
    month1=now_date.month
    day1=now_date.day 
    if day1<10:
        day1 = str('0')+str(day1)
    else:
        str(day1)
    if month1<10:
        month1 = str('0')+str(month1)
    else:
        str(month1)
        
    print  str(day1) + str(month1) + str(year1)
    html_doc = urlopen('https://lenta.ru/%d/%s/%s' % (year1,month1,day1)).read()
       
    soup = BeautifulSoup(html_doc, "lxml")
   # ws.write(0, t, str(day1) + '.' + str(month1) + '.' + str(year1) )
    
 
    for link in soup.find_all('a'):
        detal_link = link.get('href')
        result = re.findall(r'/news/%d/%s/%s/\w+/' % (year1,month1,day1), detal_link)
        if result: 
            #дебильный способ сложить ссылку        
            z=0
            site='https://lenta.ru'
            for det_link in result:
                site=site + result[z]
                z=z+1
            
            html_doc = urlopen(site).read()        
            soup = BeautifulSoup(html_doc, "lxml")
            
            #очищаем текст
            text_detal = [child.strip() if isinstance(child, str) else str(child) for child in soup.find('div', attrs={'class': 'b-text clearfix'})]
            text_detal = ''.join(text_detal)
            clear_text_detal=''.join(BeautifulSoup(text_detal).findAll(text=True))
            text_one_day = text_one_day + clear_text_detal
            #Для разбития на токены
            #list_word = tknzr.tokenize(clear_text_detal)
    #print text_one_day        
    
    list_word = nltk.word_tokenize(text_one_day)
    #print list_word
    #оставили символы больше 3
    for res_word in list_word:
        if len(res_word)>3 and res_word.isalpha():
                   #print res_word
            finish_word.append(res_word)
            #---csv
            #нормализация слов
    for word in finish_word:
        word_normal= morph.parse(word)[0]
        n_word.append(word_normal.normal_form)
    #print word_normal.normal_form
                
    filtered_words = [word for word in n_word if word not in get_stop_words('russian')]
    #print  n_word
            
    c = FreqDist(filtered_words)
    y=0
#    k=1
#    we=1
    if i==0:
        for key, value in c.items():        
#            while key:
#                globals()[key]=[]
#                globals()[key] = globals()[key].append(key)
#                globals()[key] = globals()[key].append(value)
#                #y=y+1
            print key, " ", value
#        print globals()[key]
#            mas = []
#            for i in range(3):
#                mas.append([value])
#                for j in range(2):
#                    mas[i].append(key)
#                    #r += 1  # Чтобы заполнялось не одно и тоже
#            
#            print(mas)
#        if i==0:
#            ws.write(k, cv, key)
#            ws.write(k, cv+1, value)
#        else:
#            while True:
#                if ws.row_values(we)[0]==key:
#                    ws.write(we,cv,value)
#                    break
#                else:
#                   ws.write(we+1, cv, key)
#                   ws.write(we+1, cv, value)
#                   break
#                we=we+1
        #ws.write(k, cv+1, value)
#        k=k+1 
    now_date = now_date+delta
#    cv=cv+2
    #print now_date    
    text_one_day = ''
    i=i+1
    
#wb.save('D:\\test.xls')

            #print c
           # j=0        
            #for p in c:
              #  ws.write(j, 0, c.items())
          #  j=j+1
       # wb.save('news.xls')
     
        
         
         
        