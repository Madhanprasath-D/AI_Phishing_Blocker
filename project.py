import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
df=pd.read_csv('dataset.csv')
X=df.drop(columns='status')
Y=df['status']
X_train,Y_train,X_test,Y_test=train_test_split(test_size=0.3,random_state=40)

