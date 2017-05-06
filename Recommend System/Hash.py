def sti(s):
	return abs(hash(str(s))) % (10 * 8)

import pandas as pd
col_name = ['uid','bid','rate','rid']
df = pd.read_csv('D:/Workplace/BigData/yelp_academic_dataset_review_trim.txt', sep =',', names=col_name)

df['uid'] = sti(df['uid'])
df['bid'] = sti(df['bid'])
df['rid'] = sti(df['rid'])

for i in range(1,100):
    print(df['uid',i])