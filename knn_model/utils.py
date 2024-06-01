import pickle, pandas, numpy, os
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

model = pickle.load(open(f'{os.getcwd()}/knn_model/trained_models/model_v1.0.0.pkl', 'rb'))
scaler = pickle.load(open(f'{os.getcwd()}/knn_model/trained_models/scaler.pkl', 'rb'))

def preprocessing(obj):
    obj = pandas.DataFrame(obj)
    print(obj)
    obj[['BMI', 'Age']] = scaler.transform(obj[['BMI', 'Age']])
    print(obj)
    return obj.drop('outcome', axis=1)

def predict(data):
    print(data)
    temp = model.predict(data)
    print(model)
    print(temp)
    return temp
