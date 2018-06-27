import pandas as pd
import pickle
import os

# Load Machine Learning Models
print("Load Machine Learning Models")
dirname = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(dirname,'models','svm.pkl'), 'rb') as f1:
    svc = pickle.load(f1)
with open(os.path.join(dirname,'models','vect.pkl'), 'rb') as f2:
    vect = pickle.load(f2)

"""
predicts the sentiment expressed by a tweet '+', '-' or '='
"""
def predictFrench(tweet):
    instance = pd.DataFrame(vect.transform([tweet]).todense(),columns=vect.get_feature_names())
    return svc.predict(instance)[0]