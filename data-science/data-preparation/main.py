import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

data = pd.read_csv('data.csv')

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')


def calculateMissingValues(data, imputer, beginIndex, endIndex):
    temp = data.iloc[:, beginIndex:endIndex].values
    imputer = imputer.fit(temp[:, beginIndex:endIndex])
    temp[:, beginIndex:endIndex] = imputer.transform(
        temp[:, beginIndex:endIndex])
    return temp


# print(calculateMissingValues(data, imputer, 1, 4))
