# coding: utf-8
import pandas as pd

col_name = ['id', 'phone', 'credit_card_id', 'unknown', 'address', 'card', 'gender', 'age',\
			'brand', 'product', 'amount', 'price', 'store', 'time', 'date']
df = pd.read_csv('D:/data.txt', sep=',',\
                 names=col_name, usecols=['phone', 'store', 'date'])

df['phone'] = df['phone'].astype('str')
df['phone'] = df['phone'].map(lambda x: x.rstrip('.0'))
df = df.drop_duplicates()

df['month'] = df['date'].map(lambda x: int(x.split('.')[1]))
df['day'] = df['date'].map(lambda x: int(x.split('.')[2]))
del df['date']

df['store'] = df['store'].astype('category')
cat_columns = df.select_dtypes(['category']).columns
df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)
print(df['store'].nunique())

df.to_csv('D:/tdata.txt', index=False)