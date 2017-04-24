# coding: utf-8
import pandas as pd

col_name = ['id', 'phone', 'credit_card_id', 'unknown', 'address', 'card', 'gender', 'age',\
			'brand', 'product', 'amount', 'price', 'store', 'time', 'date']
df = pd.read_csv('data.txt', sep=',', names=col_name, usecols=['phone', 'store', 'date'])

df['phone'] = df['phone'].astype('str')
df['phone'] = df['phone'].map(lambda x: x.rstrip('.0'))
df = df.drop_duplicates()

df.to_csv('trimed_data.txt', index=False)