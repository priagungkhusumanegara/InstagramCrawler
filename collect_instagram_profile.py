__author__ = "Priagung Khusumanegara"
__copyright__ = "Copyright 2018, Instagram Crawler"
__credits__ = ["instabot"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Prigung Khusumanegara"
__email__ = "priagung.123@gmail.com"
__status__ = "Development"

# lib
import os
import sys
import pandas as pd
from pandas.io.json import json_normalize
from instabot import Bot

# Your Username and Password 
bot = Bot()
bot.login(username= "<username>" , password="<password>")

# dataframe
data = pd.DataFrame([])

# list of target name
with open('list_of_name.txt') as f:
    content = f.readlines()


content = [x.strip() for x in content] 

# append list of username from target list
for val in content:
    bot.search_users(val)
    jsondata = bot.last_json
    X = json_normalize(jsondata['users'])
    if len(X) > 0:
        Y = X.assign(Name=val)
        Z = Y.iloc[0]
        data = data.append(Z)
    else:
        pass

print(data)
