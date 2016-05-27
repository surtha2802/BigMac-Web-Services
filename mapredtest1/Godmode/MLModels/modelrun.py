#!usr/local/spark/python
from pyspark import SparkContext

from pyspark.mllib.regression import LabeledPoint
import numpy as np
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel
from pyspark.mllib.classification import SVMWithSGD, SVMModel
sc=SparkContext("local")
from pyspark.mllib.classification import LogisticRegressionWithLBFGS, LogisticRegressionModel
import os
features=open("/root/Desktop/features.LOL","r")
feature=features.read().strip().split(' ')
i=map(lambda x:float(x),feature)


param=open("/root/Desktop/parameters.LOL","r")
temp=param.readlines()
print "LOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOL"
supermodel=temp[2].strip()
Modelname = LinearRegressionModel.load(sc, supermodel)

print Modelname.predict(i),"ijfksfksnfknfn jncjnnfknsklfnsk"
r=str(Modelname.predict(i))
ss="echo %s >/root/Desktop/predicted.txt" %r
os.system(ss)








