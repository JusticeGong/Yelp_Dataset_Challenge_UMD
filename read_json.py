import pandas as pd
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

chenckin = pd.read_json('XXX.json', lines=True, encoding='utf-8')

print(chenckin.head(50))