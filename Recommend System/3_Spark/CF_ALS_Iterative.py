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
    #print(i)
    if i == 1:
        j = 4
    elif i == 2:
        j = 6
    else:
        j = 8
    for j in range (1, j):
        #print(j)
        index = str(i) + str(j)
        if index not in ['21', '31', '32', '35']:
            inputpath = ("file:/home/gz/Desktop/BigDataProject/Dataset/SubModelDataset" + str(index) + ".txt") 
            # Load and parse the data
            data = sc.textFile(inputpath)
            ratings = data.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))
            # Build the recommendation model using Alternating Least Squares
            # Find best iteration num among (1:10):
            for numIterations in range(1,11):
                rank = 10
                model = ALS.train(ratings, rank, numIterations)
                # Evaluate the model on training data
                testdata = ratings.map(lambda p: (p[0], p[1]))
                predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
                ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
                MAPE = ratesAndPreds.map(lambda r: abs(r[1][0] - r[1][1])/r[1][0]).mean()
                print('SubModel = ' + str(index) + ', numIteration = ' + str(numIterations) + ', MAPE = ' + str(MAPE))
                MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
                print('SubModel = ' + str(index) + ', numIteration = ' + str(numIterations) + ', MSE = ' + str(MSE))
                # Savemodel
                outputpath = "BigDataProject/Models/Model" + str(index) + "_numIteration_" + str(numIterations)
                model.save(sc, outputpath)



