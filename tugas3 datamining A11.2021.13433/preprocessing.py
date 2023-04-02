import numpy as np
import matplotlib.pyplot as plt
import sklearn
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv(
    "Data.csv")
x = dataset.iloc[:, :-2].values
y = dataset.iloc[:, [3, 4]]
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])


ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
le = LabelEncoder()
y = y.apply(LabelEncoder().fit_transform)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x[:, 3:] = sc.transform(x[:, 3:])
# print(x)
print("\n")
# print(y)
print(x_train)
print(x_test)
# print(y_train)
# print(y_test)
