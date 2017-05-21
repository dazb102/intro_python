# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:42:53 2017

@author: Wu
"""

import os
os.chdir('c:/coding/practice')

#8.1
test1='This is a test of the emergency text system'
with open('test.txt','w') as outFile:
    outFile.write(test1)

#8.2    
with open('test.txt','r') as inFile:
    print(inFile.read()==test1)


#8.3
import csv
content='''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"'''

with open('book.csv','w') as outFile:
    outFile.write(content)

#8.4  
with open('book.csv','r') as inFile:
    readCon=csv.DictReader(inFile)
    for x in readCon:
        if x['author']=='Lynne Truss':
            print(x['book']=='Eats, Shoots & Leaves')
        else:
            pass
# 8.5    
content=u'''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''

with open('books.csv','w',encoding='utf8') as outfile:
    outfile.write(content)
    
#8.6
import sqlite3
con=sqlite3.connect('books.db')
cur=con.cursor()
try:
    cur.execute('drop table books;')
except:
    pass
cur.execute('create table books(title text, author text, year integer);')

#8.7
with open('books.csv','r',encoding='utf8') as infile:    
    content=csv.reader(infile)
    next(content) #skip first row
    content=[x for x in content]
cur.executemany('insert into books values(?,?,?)',content)

#8.8
title=cur.execute('select title from books order by title').fetchall()
for x in title:
    print(x)
    
#8.9
books=cur.execute('select * from books order by year').fetchall()
for a,b,c in books:
    print(a,b,c)

con.commit()
con.close()

#8.10
import sqlalchemy as sa
con=sa.create_engine('sqlite:///books.db')
for x in con.execute('select title from books order by title'):
    print(x)
    
#8,11
import redis
#be sure your redis server is up running
con=redis.Redis()
con.hmset('test',{'count':1,'name':'Fester Bestertester'})
con.hvals('test')

#8,12
#hash in Redis can only save stirng, thus incr method was unsupported
con.hset('test','count',int(con.hget('test','count'))+1)
con.hget('test','count')
print(con.hgetall('test'))



      