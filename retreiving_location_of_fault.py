# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 08:07:18 2023

@author: TECHIE
"""

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import ssl
import numpy as np

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address=input('Enter the location of the road: ')
address = address.strip()


parms = dict()
parms["address"] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))


try:
        js = json.loads(data)
except:
    print(data)  # We print in case unicode causes an error
    
if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
    print('==== Failure To Retrieve ====')
    print(data)
print('Final Data=', data)

###########################################################################
# HERE WE GOT that has the 'js' that do contain the latitude and longitude.
location=js['results'][0]['geometry']['location']
print('\n\n','-'*50, '\nLocation= ', location)
latlng=np.array([[location['lat']], [location['lng']]]).transpose()

###########################################################################

# NOW UNPICKLE THE THE STANDARD_SCALER AND KNN MODEL TO PREDICT THE CLUSTER CENTRE. 
import joblib
st_x=joblib.load(r'C:\Users\TECHIE\Desktop\Project\old one\fitted_Standard_Scaler.pkl')
classifier=joblib.load(r'C:\Users\TECHIE\Desktop\Project\old one\knn_model.pkl')


#feature Scaling  
latlng=st_x.transform(latlng)


cluster_predicted=classifier.predict(latlng)
print('predicted cluster =',cluster_predicted)
