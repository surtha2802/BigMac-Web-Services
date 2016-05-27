import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn


from sklearn.datasets import load_boston
boston=load_boston()
bos=pd.DataFrame(boston.data)



from sklearn.linear_model import LinearRegression


import pickle

hp=pickle.loads(houseprice)
print bos.target.head(1)
print hp.predict(bos.head(1))
