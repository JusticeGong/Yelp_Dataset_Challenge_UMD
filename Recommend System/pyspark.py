from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("CF")
conf = (conf.setMaster('local[*]')\
.set("spark.driver.memory", "8g")\
.set("spark.executor.memory", "8g")\
.set("spark.driver.allowMultipleContext", "true"))
sc = SparkContext(conf=conf)


# Load and parse the data
data = sc.textFile("file:/home/gz/Documents/yelp.txt")
ratings = data.map(lambda l: l.split(','))\
    .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))

# Build the recommendation model using Alternating Least Squares
# for numIterations in range (1,16):
rank = 10
numIterations = 15
model = ALS.train(ratings, rank, numIterations)
# Evaluate the model on training data
testdata = ratings.map(lambda p: (p[0], p[1]))
predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
# MAPE = ratesAndPreds.map(lambda r: abs(r[1][0] - r[1][1])/r[1][0]).mean()
# print('********************************************************** The interation = '+ str(numIterations) + ' and MAPE is ' + str(MAPE))



# MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
# print("Mean Squared Error = " + str(MSE))

# Save and load model
model.save(sc, "CF0507/Model_iteration15")
m = MatrixFactorizationModel.load(sc, "CF0507/Model_iteration15")


#Write result to file
def toCSVLine(data):
  return ','.join(str(d) for d in data)

lines = predictions.map(toCSVLine)
lines.saveAsTextFile('Result/I15_0507')