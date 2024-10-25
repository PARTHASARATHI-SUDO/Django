import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import PassiveAggressiveRegressor
import warnings
import matplotlib.pyplot as plt, seaborn as sns
warnings.filterwarnings('ignore')
import math
data = pd.read_csv('ongc.csv')
data.groupby('internal corrosion')['maintenance time(days)'].aggregate(['mean','median']).plot.bar()
plt.show()



#
# def algorithm(datas):
#     data = pd.read_csv('ongc.csv')
#     data_x = data.iloc[:, :-1]
#     data_y = data.iloc[:, -1]
#     string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]
#
#     LabelEncoders = []
#     for i in string_datas:
#         newLabelEncoder = LabelEncoder()
#         data_x[i] = newLabelEncoder.fit_transform(data_x[i])
#         LabelEncoders.append(newLabelEncoder)
#     ylabel_encoder = None
#     if type(data_y.iloc[1]) == str:
#         ylabel_encoder = LabelEncoder()
#         data_y = ylabel_encoder.fit_transform(data_y)
#
#     model = PassiveAggressiveRegressor()
#     model.fit(data_x, data_y)
#     value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
#     l = 0
#     for i in string_datas:
#         z = LabelEncoders[l]
#         value[i] = z.transform([value[i]])[0]
#         l += 1
#     value = [i for i in value.values()]
#     predicted = model.predict([value])
#     if ylabel_encoder:
#         predicted = ylabel_encoder.inverse_transform(predicted)
#     return predicted[0]
#
#
#
# a = algorithm(['seamless', 600, 'no', 'no', 'portable', 'no coating', 'pipe or weld material failure'])
# print(math.floor(a))

# s = '** python program **'
# # print(s.endswith('m'))
# print(s.rstrip('m'))

# file1 = open("MyFile.txt","x")
# file1.close()

# A = ["Python is easy to learn.\n", "I want to become python developer\n", "Python with django framework have good scope.\n", "It is difficult in starting stage.\n"]
#
# # Writing on our file:
# f = open('file1.txt', 'w')
# f.writelines(A)
# f.close()
#
# # Using readlines() function
# f = open('file1.txt', 'r')
# lines = f.readlines()
#
# for line in lines:
#     if line[0] != 'P':
#         print(line)

# a = [5.0, 81.0, 43.0, 36.0, 55.0]
#
# x = list(map((lambda n: n**0.5), a))
# print(x)
#
# y = filter((lambda c, d: c==d if c**))
# # m = []
# for i in x:
#     count = 0
#     if i**2 == a[count]:
#         m.append(a[count])
#         count += 1
# print(m)


