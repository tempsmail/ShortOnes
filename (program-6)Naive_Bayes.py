import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

iris=load_iris()
print("features : ",iris.feature_names)
print("labels : ",iris.target_names)

x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.30,random_state=109)

GNB=GaussianNB()
GNB.fit(x_train,y_train)
y_pred=GNB.predict(x_test)

print(y_pred)
print('accuracy score : ',accuracy_score(y_test,y_pred))
