# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:58:59 2020

@author: Bella
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

YT = pd.read_csv("us-states.csv")

YT

YT.columns

YT['valid'] = YT['state'] == "Pennsylvania"

YT = YT[YT.valid == True]

YT

YT.dtypes



YT['valid'] = YT['date'] != "2020-04-21"
YT = YT[YT.valid == True] 
YT['valid'] = YT['date'] != "2020-04-22"
YT = YT[YT.valid == True]

adj_Deaths = pd.Series(YT['deaths'])

YT['adj_deaths'] = adj_Deaths
YT.to_csv("us-states.csv", index = False)

YT

YT['date'] = pd.to_datetime(YT['date'],
                              infer_datetime_format=True)

YT['date']

locator = mdates.AutoDateLocator(minticks=15,maxticks=30)
formatter = mdates.ConciseDateFormatter(locator)

fig, ax = plt.subplots() 
ax.bar(YT['date'], YT['adj_deaths'],width=.87,color='steelblue', align='center')
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_major_locator(locator)
ax.set_ylabel('Cumulative Deaths')
ax.set_xlabel('Date')
ax.set_title('Pa. coronavirus deaths')
plt.show()

