import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from collections import OrderedDict
from sklearn.metrics import accuracy_score

df = pd.read_csv('phase2_df.csv')

x_columns = ['slap',
             'harass_scale',
             'power_scale',
             'push_shove',
             'limit_family_contact',
             'kick_punch',
             'jealous',
             'perp_arrested_ever',
             'num_threats',
             'level_severity',
             'rape_ever',
             'life_danger',
            ]

X = df[x_columns]
y = df[['reassault']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .15, random_state = 0, stratify=y)

clf = LogisticRegressionCV(cv=5,
                           random_state=0,
                          ).fit(X_train, y_train)

print('Accuracy of Logistic Regression classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))

print('Accuracy of Logistic Regression classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))

def predictorizer(feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12):

    new_data = OrderedDict([ 
        ('slap', feature1),
        ('harass_scale', feature2),
        ('power_scale', feature3),
        ('push_shove', feature4),
        ('limit_family_contact', feature5),
        ('kick_punch', feature6),
        ('jealous', feature7),
        ('perp_arrested_ever', feature8),
        ('num_threats', feature9),
        ('level_severity', feature10),
        ('rape_ever', feature11),
        ('life_danger', feature12),
        ])
    # .values.reshape(1, -1) because it must be 2-dim, because we passed only one new observation
    new_data = pd.Series(new_data).values.reshape(1,-1) 
    # Use the model to make a prediction
    prediction = clf.predict_proba(new_data)[[0],[1]]
    if prediction < 1:
        prediction_string = '10'
    if prediction < .9:
        prediction_string = '9'
    if prediction < .8:
        prediction_string = '8'
    if prediction < .7:
        prediction_string = '7'
    if prediction < .6:
        prediction_string = '6'
    if prediction < .5:
        prediction_string = '5'
    if prediction < .4:
        prediction_string = '4'
    if prediction < .3:
        prediction_string = '3'
    if prediction < .2:
        prediction_string = '2'
    if prediction < .1:
        prediction_string = '1'
    return prediction_string


print(predictorizer('0','0','0','0','0','0','0','0','0','0','0','0',))

