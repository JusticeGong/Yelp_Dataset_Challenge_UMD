#Import Package, set configuration

from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("CF")
conf = (conf.setMaster('local[*]')\
.set("spark.driver.memory", "8g")\
.set("spark.executor.memory", "8g")\
.set("spark.driver.allowMultipleContext", "true"))
sc = SparkContext(conf=conf)

n = 0
query = []
index = '0'
modelpath = 'BigDataProject/SubModels/Model0' + str(index)
m = MatrixFactorizationModel.load(sc, modelpath)
inputpath = ("file:/home/gz/Desktop/BigDataProject/PredOutput/PredOutput0.txt")
outputpath = ("/home/gz/Desktop/BigDataProject/PredOutput/PredOutput1.txt")

data = sc.textFile(inputpath)
ratings = data.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))

testdata = ratings.map(lambda p: (p[0], p[1]))
predictions = m.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
a = ratesAndPreds.collect()
with open (outputpath, 'w') as w:
    w.write(str(a))
    w.close

