import pandas as pd
# Importing the dataset2
dataset2 = pd.read_csv('env/static/percent.csv')
X = dataset2.iloc[:,[7,8,9,12,13,14]].values
y = dataset2.iloc[:, 15].values

# Splitting the dataset22 into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scalin2g
from sklearn.preprocessing import StandardScaler
sc2 = StandardScaler()
X_train = sc2.fit_transform(X_train)
X_test = sc2.transform(X_test)


# Training the dataset22
from sklearn.linear_model import LogisticRegression
lin2 = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial')
lin2.fit(X_train,y_train)

# Testing the dataset2 on trained model
y_pred = lin2.predict(X_test)
score = lin2.score(X_test,y_test)*100
print("L Probability:" , score)

# Testing with a custom input
import numpy as np
new_prediction = lin2.predict_proba(sc2.transform(np.array([[200,0,25,23,52,400]])))
print("Chasing Probability:" , new_prediction[0][1]*100)

