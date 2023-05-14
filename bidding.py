# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:31:01 2023

@author: TECHIE
"""


import sqlite3 as sql
import pandas as pd
import numpy as np
import time

db=sql.connect(r'C:\Users\TECHIE\Desktop\Project\Project_databases.db')
cur=db.cursor()

import retreiving_location_of_fault as level_finder
level=level_finder.get_local()

cur.execute('''
            SELECT serial_number, state_name, facility_name FROM contractor_database WHERE clusters=%d
            '''%level)
result=cur.fetchall()
#print(result)

serial_no=[row[0] for row in result]
result=[list(tup[1:]) for tup in result]

result=pd.DataFrame(result, columns=['state_name', 'name'], index=serial_no)

Threshold=100000
result['bid']=np.NAN
result['time']=np.NAN
###############################################################################
#ALLOW BIDDING HERE
###############################################################################
# TEMP CODE
import random
some_people_bid=random.randrange(20, len(result))
print('people bidded=',some_people_bid)
randomlist = random.sample(serial_no, some_people_bid)
#print(randomlist)
for cid in randomlist:
    bid=random.randrange(10000,10000000)
    if bid<Threshold:
        #print(bid, "has Bid too small")
        pass
    else:
        result.loc[cid, 'bid']=bid
        result.loc[cid, 'time']=time.time()
##################################################################################

min_bid=np.nanmin(result.loc[:, 'bid'])
print('min bid done=',min_bid)

final=result[result['bid']==min_bid]
min_time=np.min(final.loc[: ,'time'])
final=final[final['time']==min_time]

print('The contractor allowed to bid has details:\n'+str(final))
print('The contractor index is:',final.index[0])