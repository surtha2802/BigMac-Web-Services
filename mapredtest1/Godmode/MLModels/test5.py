import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_boston
boston=load_boston()
print boston.keys(),"keys kjkjdsajadkjkjkdj"

print boston.feature_names

print boston.DESCR

bos=pd.DataFrame(boston.data)
#bos.head()

bos.columns=boston.feature_names
print bos.head(),"head 5"

print "target",boston.target[:5]
bos['PRICE']=boston.target

print bos.head(),"head 5"


from sklearn.linear_model import LinearRegression
X=bos.drop('PRICE',axis=1)

#lm=LinearRegression()

#lm.fit(X,bos.PRICE)


#print "intercept   ",lm.intercept_
#print "no of coeff  ",lm.coef_


#temp=pd.DataFrame(zip(X.columns,lm.coef_),columns = ['features','estimatedCoefficients'])
#print temp
'''
plt.scatter(bos.RM, bos.PRICE)
plt.xlabel("average nnnnn")
plt.ylabel("house price")
plt.show()

print lm.predict(X)[:5],"predicted"

print "target",boston.target[:5],"actual"



plt.scatter(lm.predict(X),bos.PRICE)
plt.xlabel("predicted nnnnn")
plt.ylabel("house price")
plt.show()


mseFull=np.mean((bos.PRICE-lm.predict(X))**2)

print mseFull,"mse error"

'''

X_train,X_test,Y_train,Y_test=sklearn.cross_validation.train_test_split(X,bos.PRICE,test_size=0.33,random_state=5)
print X_train.shape
print X_test.shape
print Y_train.shape
print Y_test.shape
print "llllllllllllllllllllllllllllll"
lm=LinearRegression()
lm.fit(X_train,Y_train)

print Y_test.head(5),"hhhhhhhhh"
print "kkkkkkkkkkkkkkkkkkkkkkkkkkk"
print lm.predict(X_test.head(5))
#pred_train=lm.predict(X_train)






#pred_test=lm.predict(X_test)

#print pred_train[:5]
#print pred_test[:5]
#bos.drop('PRICE',axis=1)
#bos.columns=boston.feature_names

#print X.columns
from sklearn.externals import joblib
joblib.dump(lm, 'filename.pkl')
#import pickle
#houseprice = pickle.dumps(lm)
#clf2 = pickle.loads(s)
#clf2.predict(X[0:1])


#print lm.predict(X_train.head(5))

#





