import pickle, pandas, numpy, os
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

df = pickle.load(open(f'{os.getcwd()}/knn_model/trained_models/dataframe.pkl', 'rb'))
model = pickle.load(open(f'{os.getcwd()}/knn_model/trained_models/model_v1.0.0.pkl', 'rb'))

def preprocessing(obj):
    # print(df)
    obj = pandas.DataFrame(obj, index=[df.shape[0]])
    print(df.shape)
    print(obj)
    new_df = pandas.concat([df, obj])
    # print(new_df.tail(1))
    scaler = MinMaxScaler()
    new_df[['BMI', 'Age']] = scaler.fit_transform(new_df[['BMI', 'Age']])
    print(new_df.tail(1))
    return new_df.tail(1).drop('outcome', axis=1)

def predict(data):
    print(data)
    temp = model.predict(data)
    print(model)
    print(temp)
    return temp
