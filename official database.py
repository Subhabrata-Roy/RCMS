# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 21:33:51 2022

@author: TECHIE
"""


import sqllite3 as sql

conn=sql.connect('C:\\Users\\TECHIE\\Desktop\\Project\\Project_databases.db')

cur=conn.cursor()

cur.executescript('''
            DROP TABLE IF EXISTS officer_database;
            
            CREATE TABLE officer_database(
                Uid    primary key,
                Name   text,
                cluster numeric
            );
            ''')
conn.commit()
conn.close()