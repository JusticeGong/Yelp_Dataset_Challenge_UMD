import pandas as pd
j_cols = ['business_id', 'user_id', 'review_id', 'stars']
users = pd.read_json('D:/Workplace/BigData/yelp_academic_dataset_review_trim.json', encoding='utf8')
print(users.head(50))


from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating