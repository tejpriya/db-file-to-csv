from django.contrib.auth.models import *
from con1.models import * 
import csv
from django.shortcuts import render,redirect
from django.http import HttpResponse
import sqlite3
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
def create(cursor):
    cursor.execute(""" CREATE TABLE con(name VARCHAR(200) NOT NULL)""")
    print("table created")
    conn.commit()
def insert(qry,abc):
    qry="insert into con(name)values('sai');"
    conn.commit() 

def select(qry):
    qry="select * from con;"  
    
def index(request):
    return render(request,"D:/cosai/scon/scon/templates/index.html")

def export_users_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['content=Disposition']='attachment;filename="con.csv"'
    
    writer=csv.writer(response)
    writer.writerow(['name'])
    
    con=s1.objects.all().values_list('name')
    for co in con:
        writer.writerow(co)
    
    
    return response