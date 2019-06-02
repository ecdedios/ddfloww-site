import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from collections import OrderedDict
from sklearn.metrics import accuracy_score

df = pd.read_csv('phase1_df.csv')
print(df.head())

x_columns = ['threat_hit',
             'controlled_ever',
             'jealous',
             'location_tracking',
             'thrown_object'
            ]

X = df[x_columns]
y = df[['abuse_past_year']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .15, random_state = 0, stratify=y)

clf = LogisticRegressionCV(cv=5,
                           random_state=0,
                          ).fit(X_train, y_train)

# print('Accuracy of Logistic Regression classifier on training set: {:.2f}'
#      .format(clf.score(X_train, y_train)))

# print('Accuracy of Logistic Regression classifier on test set: {:.2f}'
#      .format(clf.score(X_test, y_test)))

def predictorizer(feature1, feature2, feature3, feature4, feature5):

    new_data = OrderedDict([ 
        ('threat_hit', feature1),
        ('controlled_ever', feature2),
        ('jealous', feature3),
        ('location_tracking', feature4),
        ('thrown_object', feature5)
        ])
    # .values.reshape(1, -1) because it must be 2-dim, because we passed only one new observation
    new_data = pd.Series(new_data).values.reshape(1,-1) 
    # Use the model to make a prediction
    return str(clf.predict(new_data)[0])

print(predictorizer(0,0,0,0,0))

