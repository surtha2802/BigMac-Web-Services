#!usr/local/spark/python
from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
import numpy as np
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel
sc=SparkContext("local")




# Load and parse the data
def parsePoint(line):
	#values = [float(x) for x in line.replace(',', ' ').split(' ')]
	values=line.split(',')
	return LabeledPoint(values[2:3], values[0:2]+values[3:])

data = sc.textFile("/root/Desktop/dataset/kc_house_data.csv")
parsedData = data.map(parsePoint)

# Build the model
model = LinearRegressionWithSGD.train(parsedData, iterations=100, step=0.00000001)

# Evaluate the model on training data
valuesAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
MSE = valuesAndPreds.map(lambda (v, p): (v - p)**2).reduce(lambda x, y: x + y) / valuesAndPreds.count()
print("Mean Squared Error = " + str(MSE)+"bkbkbbbbbbbbbbbbbbbbbbbbbbbbkkbkbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbkbkbkb")



# Save and load model
model.save(sc, "myModelPath")
sameModel = LinearRegressionModel.load(sc, "myModelPath")


