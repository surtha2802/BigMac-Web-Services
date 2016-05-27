import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.externals import joblib
import pickle
from sklearn.datasets import load_boston
boston=load_boston()
bos=pd.DataFrame(boston.data)



from sklearn.linear_model import LinearRegression
hp = joblib.load('filename.pkl') 



#hp=pickle.loads(houseprice)
print boston.target[:5]

print hp.predict(bos.head(5))


bos.columns=boston.feature_names
print bos.head(),"head 5"

