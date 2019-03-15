#! /usr/bin/env python
import psycopg2

DBNAME = "news"


def execute_query(query):
    ''' Execute a query to the news database '''
    db = psycopg2.connect(database=DBNAME, user="vagrant", password="vagrant")
    cur = db.cursor()
    cur.execute(query)
    return cur.fetchall()
    db.close()

# 1. What are the most popular three articles of all time?
query1 = ''' select ar.title ,count(lg.id) as views from log lg, articles ar 
where concat('/article/', ar.slug) = lg.path
group by ar.title
order by views desc
limit 3; '''

# 2. Who are the most popular article authors of all time?
query2 = ''' select au."name" ,count(lg.id) as views from log lg, articles ar, authors au
where concat('/article/', ar.slug) = lg."path" and au.id = ar.author 
group by au."name"
order by views desc; '''

# 3. On which days did more than 1% of requests lead to errors?
query3 = '''select to_char(log."time", 'YYYY-MM-DD') as date, round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),3) as percentage 
from log group by to_char(log."time", 'YYYY-MM-DD') having round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),3) > 1.0;'''


def question_1(query):
    results = execute_query(query)
    print('1. The 3 most popular articles of all time are:')
    for result in results:
        print (str(result[0]) + ' - ' + str(result[1]) + ' views')
    print('\n')


def question_2(query):
    results = execute_query(query)
    print('2. The most popular article authors of all time are:')
    for result in results:
        print (str(result[0]) + ' - ' + str(result[1]) + ' views')
    print('\n')


def question_3(query):
    results = execute_query(query)
    print('3. Days with more than 1% of request that lead to an error:')
    for result in results:
        print (str(result[0]) + ' - ' + str(result[1]) + ' %')
    print('\n')

# Display results
question_1(query1)
question_2(query2)
question_3(query3)