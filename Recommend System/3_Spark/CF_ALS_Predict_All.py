#Import Package, set configuration
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("CF")
conf = (conf.setMaster('local[*]')\
.set("spark.driver.memory", "8g")\
.set("spark.executor.memory", "8g")\
.set("spark.driver.allowMultipleContext", "true"))
sc = SparkContext(conf=conf)

m0 = MatrixFactorizationModel.load(sc, 'BigDataProject/SubModels/Model00')
m1 = MatrixFactorizationModel.load(sc, 'BigDataProject/SubModels/Model31')
m2 = MatrixFactorizationModel.load(sc, 'BigDataProject/SubModels/Model32')
m3 = MatrixFactorizationModel.load(sc, 'BigDataProject/SubModels/Model33')
m4 = MatrixFactorizationModel.load(sc, 'BigDataProject/SubModels/Model34')
m5 = MatrixFactorizationModel.load(sc, 'BigDataProject/SubModels/Model35')
m6 = MatrixFactorizationModel.load(sc, 'BigDataProject/SubModels/Model36')
m7 = MatrixFactorizationModel.load(sc, 'BigDataProject/SubModels/Model37')

inputpath = ("/home/gz/Desktop/BigDataProject/RandomUserGroup.txt")
outputpath0 = ("/home/gz/Desktop/BigDataProject/RandomUserGroupPred_25_0.txt")
outputpath1 = ("/home/gz/Desktop/BigDataProject/RandomUserGroupPred_25_1.txt")
outputpath2 = ("/home/gz/Desktop/BigDataProject/RandomUserGroupPred_25_2.txt")
outputpath3 = ("/home/gz/Desktop/BigDataProject/RandomUserGroupPred_25_3.txt")
outputpath4 = ("/home/gz/Desktop/BigDataProject/RandomUserGroupPred_25_4.txt")
outputpath5 = ("/home/gz/Desktop/BigDataProject/RandomUserGroupPred_25_5.txt")
outputpath6 = ("/home/gz/Desktop/BigDataProject/RandomUserGroupPred_25_6.txt")
outputpath7 = ("/home/gz/Desktop/BigDataProject/RandomUserGroupPred_25_7.txt")
n = 0
with open (outputpath0, 'a') as w0:
    with open (outputpath1, 'a') as w1:
        with open (outputpath2, 'a') as w2:
            with open (outputpath3, 'a') as w3:
                with open (outputpath4, 'a') as w4:
                    with open (outputpath5, 'a') as w5:
                        with open (outputpath6, 'a') as w6:
                            with open (outputpath7, 'a') as w7:
                                with open (inputpath, 'r') as r:
                                    for line in r:
                                        line = line.replace(' ','')
                                        line = line.split(',')
                                        for t in line:
                                            n = n + 1
                                            print(n, t)
                                            try:
                                                a = m0.recommendProducts(int(t),25)
                                                w0.write(str(a))
                                            except:
                                                print(0)
                                            try:
                                                a = m1.recommendProducts(int(t),25)
                                                w1.write(str(a))
                                            except:
                                                print(1)  
                                            try:
                                                a = m2.recommendProducts(int(t),25)
                                                w2.write(str(a))
                                            except:
                                                print(2)
                                            try:
                                                a = m3.recommendProducts(int(t),25)
                                                w3.write(str(a))
                                            except:
                                                print(3)
                                            try:
                                                a = m4.recommendProducts(int(t),25)
                                                w4.write(str(a))
                                            except:
                                                print(4)
                                            try:
                                                a = m5.recommendProducts(int(t),25)
                                                w5.write(str(a))
                                            except:
                                                print(5)
                                            try:
                                                a = m6.recommendProducts(int(t),25)
                                                w6.write(str(a))
                                            except:
                                                print(6)
                                            try:
                                                a = m7.recommendProducts(int(t),25)
                                                w7.write(str(a))
                                            except:
                                                print(7)
                                w7.close()
                            w6.close()
                        w5.close()
                    w4.close()
                w3.close()
            w2.close()
        w1.close()
    w0.close()


