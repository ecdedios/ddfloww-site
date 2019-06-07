import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from collections import OrderedDict
from sklearn.metrics import accuracy_score

df = pd.read_csv('phase2_df.csv')

x_columns = ['slap',
             'threat_object',
             'beaten',
             'limit_family_contact',
             'kick_punch',
             'threat_hit',
             'push_shove',
             'jealous',
             'life_danger'
             ]

X = df[x_columns]
y = df[['reassault']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .15, random_state = 0, stratify=y)

clf = LogisticRegressionCV(cv=5,
                           random_state=0,
                           solver='liblinear'
                          ).fit(X_train, y_train)


print('Accuracy of Logistic Regression classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))

print('Accuracy of Logistic Regression classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))

def predictorizer(feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9):

    new_data = OrderedDict([ 
        ('slap', feature1),
        ('threat_object', feature2),
        ('beaten', feature3),
        ('limit_family_contact', feature4),
        ('kick_punch', feature5),
        ('threat_hit', feature6),
        ('push_shove', feature7),
        ('jealous', feature8),
        ('life_danger', feature9,)
        ])
    # .values.reshape(1, -1) because it must be 2-dim, because we passed only one new observation
    new_data = pd.Series(new_data).values.reshape(1,-1) 
    # Use the model to make a prediction
    prediction = str(clf.predict_proba(new_data)[[0],[1]])
    prediction = prediction.replace('[','')
    prediction = prediction.replace(']','')
    prediction = "{:.1%}".format(float(prediction))
    return prediction


print(predictorizer('1','1','1','1','1','1','1','1','1'))

