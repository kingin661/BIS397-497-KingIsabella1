# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:01:59 2020

@author: Bella
"""
import pandas as pd

YT = pd.read_csv("Yellow_Sample.csv")

YT

YT.columns

YT.dtypes

YT['VendorID']


YT[['tpep_pickup_datetime','tpep_dropoff_datetime']].dtypes

YT['tpep_pickup_datetime'].head()

YT['pickup'] = pd.to_datetime(YT['tpep_pickup_datetime'],
                              infer_datetime_format=True)

YT['pickup'].head()

del YT['tpep_pickup_datetime']

YT['dropoff'] = pd.to_datetime(YT['tpep_dropoff_datetime'],
                              infer_datetime_format=True)

del YT['tpep_dropoff_datetime']

YT['duration'] = YT['dropoff'] - YT['pickup']

YT[['pickup','dropoff','duration']].head()


pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Deleting rows where trip distacne is less than 100 

YT['trip_distance'].describe()

YT['valid'] = YT['trip_distance'] <= 100

YT[['trip_distance','valid']].head()

YT['trip_distance'].describe()

YT = YT[YT.valid == True]

print(f'   Trip Distances   ')

print(YT['trip_distance'].describe())

print()


#Delete any rows where passenger = 0 

YT['passenger_count'].describe()

YT['valid'] = YT['passenger_count'] = 0

YT[['passenger_count','valid']].head()

YT['passenger_count'].describe()

YT = YT[YT.valid == True]

print(f'   Passenger Counts   ')

print(YT['passenger_count'].describe())

print() 

#Delete any rows where trip distance = 0 

YT['trip_distance'].describe()

YT['valid'] = YT['trip_distance'] = 0

YT[['trip_distance','valid']].head()

YT['trip_distance'].describe()

YT = YT[YT.valid == True]

print(f'   Trip Distances   ')

print(YT['trip_distance'].describe())

print()

#Delete any rows w/ fare amount less than zero 

YT['fare_amount'].describe()

YT['valid'] = YT['fare_amount'] < 0

YT[['fare_amount','valid']].head()

YT['fare_amount'].describe()

YT = YT[YT.valid == True]


#Delete any rows w/ fare amount greater than 1,000

YT['fare_amount'].describe()

YT['valid'] = YT['fare_amount'] > 1000

YT[['fare_amount','valid']].head()

YT['fare_amount'].describe()

YT = YT[YT.valid == True]

print(f'   Fare Amounts   ')

print(YT['fare_amount'].describe())

print()

#Delete extra <= 0

YT['extra'].describe()

YT['valid'] = YT['extra'] <= 0

YT[['extra','valid']].head()

YT['extra'].describe()

YT = YT[YT.valid == True]

print(f'   Extra   ')

print(YT['extra'].describe())

print()

# Saving our altered data set

YT.to_csv('YT_curated.csv', index = False)



