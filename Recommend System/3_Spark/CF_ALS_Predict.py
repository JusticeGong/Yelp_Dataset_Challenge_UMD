#Import Package, set configuration

from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("CF")
conf = (conf.setMaster('local[*]')\
.set("spark.driver.memory", "8g")\
.set("spark.executor.memory", "8g")\
.set("spark.driver.allowMultipleContext", "true"))
sc = SparkContext(conf=conf)
j = 0
#Iterative train model and save model
for i in range(1,4):
    if i == 1: 
        j = 4
    elif i == 2: 
        j =6
    else: 
        j = 8
    for j in range (1, j):
        n = 0
        index = str(i) + str(j)
        print(index)
        modelpath = 'BigDataProject/SubModels/Model' + str(index)
        m = MatrixFactorizationModel.load(sc, modelpath)
        inputpath = ("file:/home/gz/Desktop/BigDataProject/Dataset/SubModelDataset" + str(index) + ".txt")
        outputpath = ("/home/gz/Desktop/BigDataProject/PredOutput/PredOutput" + str(index) + ".txt")
        data = sc.textFile(inputpath)
        ratings = data.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))
        testdata = ratings.map(lambda p: (p[0], p[1]))
        predictions = m.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
        ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
        a = ratesAndPreds.collect()
        with open (outputpath, 'w') as w:
            w.write(str(a))
            w.close




