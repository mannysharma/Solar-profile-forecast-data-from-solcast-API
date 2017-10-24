import urllib.parse
import requests
import pandas as pd
import re
import json
import csv
import numpy as np
import sys
import math
import random


#solcast API

solcast_api = "Wago92Xj-LT-SjwSQLK6cRllIQf9VlV0"

lat = -35.77
long = 149.117
capacity = 1000
output_file = 'pv_estimates'
#url of solcast

main_url = 'https://api.solcast.com.au/pv_power/estimated_actuals?'
my_parameters = {'longitude': long, 'latitude': lat, 'capacity': capacity, 'api_key': solcast_api, 'format': 'JSON'}

url4 = main_url + urllib.parse.urlencode( my_parameters )

print( url4 )

json_data = requests.get( url4 )
dict_list = json_data.json()

labels = ["period_end", "period", "pv_estimate"]

#dict_list
#print( type( dict_list ) )
#print( dict_list )
df1 = pd.DataFrame(dict_list)
#pd.DataFrame(pd.dict[dict_list], copy= True)

print(df1)
#csvfile = print( pd.DataFrame.from_dict(dict_list, orient = "columns") )

df1.to_csv("pv_output.csv", sep = " ")


#csvfile.to_csv("pv_output.csv", encoding='utf-8', sep="'")
