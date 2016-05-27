from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel
from pyspark import SparkContext
sc=SparkContext('local')
# Load and parse the data
def parsePoint(line):
    values = [float(x) for x in line.replace(',', ' ').split(' ')]
    return LabeledPoint(values[0], values[1:])

data = sc.textFile("/usr/local/spark/data/mllib/ridge-data/lpsa.data")
parsedData = data.map(parsePoint)

# Build the model
model = LinearRegressionWithSGD.train(parsedData, iterations=100, step=0.00000000001)
#iterations=100, step=0.00000001)
# Evaluate the model on training data
valuesAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
MSE = valuesAndPreds.map(lambda (v, p): (v - p)**2).reduce(lambda x, y: x + y) / valuesAndPreds.count()
print("Mean Squared Error = " + str(MSE))

print valuesAndPreds.take(100),"ndjnsjnnknsdfnsknfsndfkjnksfnsjknfjnsjknf"
print("Mean Squared Error = " + str(MSE))
# Save and load model
#model.save(sc, "myModel")
#sameModel = LinearRegressionModel.load(sc, "myModel")
