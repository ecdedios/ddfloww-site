import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from collections import OrderedDict
from sklearn.metrics import accuracy_score

df = pd.read_csv('magic_wand.csv')

x_columns = ['last_cleaned',
             'pipe_diameter',
             'num_pipe_upstream',
             'pipe_age',
             'num_spills',
             'creek_bed',
             'structural',
             'grease',
             'debris',
             'rain'
             ]

X = df[x_columns]
y = df[['sso']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .15, random_state = 0, stratify=y)

clf = LogisticRegressionCV(cv=5,
                           random_state=0,
                           solver='liblinear'
                          ).fit(X_train, y_train)


print('Accuracy of Logistic Regression classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))

print('Accuracy of Logistic Regression classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))

def predictorizer(feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10):

    new_data = OrderedDict([ 
        ('last_cleaned', feature1),
        ('pipe_diameter', feature2),
        ('num_pipe_upstream', feature3),
        ('pipe_age', feature4),
        ('num_spills', feature5),
        ('creek_bed', feature6),
        ('structural', feature7),
        ('grease', feature8),
        ('debris', feature9),
        ('rain', feature10),
        ])
    # .values.reshape(1, -1) because it must be 2-dim, because we passed only one new observation
    new_data = pd.Series(new_data).values.reshape(1,-1) 
    # Use the model to make a prediction
    prediction = str(clf.predict_proba(new_data)[[0],[1]])
    prediction = prediction.replace('[','')
    prediction = prediction.replace(']','')
    prediction = "{:.1%}".format(float(prediction))
    return prediction


print(predictorizer('0','8','3','69','8','1','0','1','1','1'))

