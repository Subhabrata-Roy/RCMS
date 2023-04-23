# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 10:57:51 2022

@author: TECHIE
"""


import sqlite3 as sql

import pandas as pd

data=pd.read_csv('C:\\Users\\TECHIE\\Documents\\colpy\\cluster_obtained.csv')
data

conn=sql.connect('C:\\Users\\TECHIE\\Desktop\\Project\\Project_databases.db')

cur=conn.cursor()

cur.executescript('''
            DROP TABLE IF EXISTS contractor_database;
            
            CREATE TABLE contractor_database(
                Serial_number      PRIMARY KEY,
                State_Name          TEXT,
                District_Name       TEXT,
                Subdistrict_Name	TEXT,
                Facility_Type       TEXT,
                Facility_Name       TEXT,	
                Facility_Address	TEXT,
                Latitude            NUMERIC,
                Longitude           NUMERIC,
                ActiveFlag_C        TEXT,
                NOTIONAL_PHYSICAL	TEXT,
                Location_Type       TEXT,
                Type_Of_Facility	TEXT,
                Nin_N	            TEXT,
                Clusters            NUMERIC
                );'''
            )

for index, row in data.iterrows():
    cur.execute('INSERT INTO contractor_database VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (index,
                      row['State Name'],
                      row['District Name'],	
                      row['Subdistrict Name'],	
                      row['Facility Type'],	
                      row['Facility Name'],	
                      row['Facility Address'],	
                      row['Latitude'],	
                      row['Longitude'],	
                      row['ActiveFlag_C'],	
                      row['NOTIONAL_PHYSICAL'],	
                      row['Location Type'],
                      row['Type Of Facility'],	
                      row['Nin_N'],	
                      row['Clusters'])
                      )
#cur.execute('SELECT COUNT(*) FROM contractor_database;')
#print(cur.fetchall())

conn.commit()
conn.close()


'''
cur.execute('SELECT * FROM contractor_database WHERE Clusters= ?',(182,))
print(cur.fetchall()) 
'''   