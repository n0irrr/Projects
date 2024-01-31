import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

traindata = pd.read_csv(r'C:\Users\Ng Zheng Chong\Projects\Binary Classification with a Bank Churn Dataset\train.csv')
factors = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
dependent = traindata.Exited
independent = traindata[factors]

"""
Bar graph showing the number of people that exited vs the number of people that did not exit
"""
def whoexit():
    exited = [0,0]
    for i in range(traindata.index.size):
        if traindata.iloc[i, 13] == 1:
            exited[0] += 1
        else:
            exited[1] += 1
    plt.figure(1,figsize=(10,10))
    plt.bar(["Exit","Did Not Exit"], exited)

"""
Scatter graph showing the credit scores of people against age
"""
def creditandage():
    age = traindata.Age
    creditscore = traindata.CreditScore

    plt.figure(2, figsize=(10,10))
    plt.scatter(age, creditscore)
    plt.xticks(np.arange(0, 102, 2))
    plt.xlabel('Age of the people(years)')
    plt.ylabel('Credit Score')

"""
Pie chart showing the composition of people from different countries
"""
#plt.pie(traindata.Geography)


#Show all graphs 
#plt.show()

print([].append(i) for i in traindata.Geography.value_counts())