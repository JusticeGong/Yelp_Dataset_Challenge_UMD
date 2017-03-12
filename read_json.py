import pandas as pd

chenckin = pd.read_json('/Users/Jacob/Desktop/Python/yelp_dataset_challenge_round9/yelp_academic_dataset_checkin.json', lines=True)

print(chenckin.head())