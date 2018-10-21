#Programme_ANN - Titanic


#Partie 1 - prepa données

# Importing the libraries
import io
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
data0 = pd.read_csv('train01.csv')

X = data0.iloc[:, [0,2,3,4,5,6,7,8,9]].values #Normal que ce soit de type object hein
y_train = data0.iloc[:, 1]

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 2] = labelencoder_X_1.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()


X_train=X
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

#On prend aussi les données de test
data0_test = pd.read_csv('test01.csv')
data_test = data0
X_test=data0_test.values


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:,1:8] = sc.fit_transform(X_train[:,1:8])
X_test[:,1:8] = sc.transform(X_test[:,1:8]) #A faire pour l_echantillon test


#Partie 2 - Construction des reseaux de neuronnes

#Importer les modules de keras
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

#Initiation
classifier=Sequential()

#Ajouter une couche d'entrée et une couche cachée
classifier.add(Dense(units=5,activation='relu',kernel_initializer='uniform',input_dim=7))
#Pour éviter le sur-apprentissage:
classifier.add(Dropout(rate=0.2))

#Ajouter une deuxième couche cachée
classifier.add(Dense(units=3,activation='relu',kernel_initializer='uniform'))
#Pour éviter le sur-apprentissage:
classifier.add(Dropout(rate=0.1))

#Ajouter la couche de sortie
classifier.add(Dense(units=1,activation='sigmoid',kernel_initializer='uniform'))

#Compiler le réseau de neuronnes
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Entrainer le réseau de neuronnes
classifier.fit(X_train[:,1:8],y_train,batch_size=10,epochs=100)

# Predicting the Test set results
y_pred = classifier.predict(X_test[:,1:8])
np.mean(y_pred) #40.18%
y_pred = np.round(y_pred[:,0]) #On met 0=Dead et 1=Survived
np.mean(y_pred) #37.76%
y_pred_final=np.eye(418,2)
y_pred_final[:,0]=X_test[:,0]
y_pred_final[:,1]=y_pred

#Exporter un fichier csv des prédictions
from xlwt import Workbook
path=r"C:\users\aymeric\documents\edx - mooc\#kaggle\titanic\mon_fichier.xls"
book=Workbook()
feuil1=book.add_sheet('feuille 1')
feuil1.write(0,0,'PassengerId')
feuil1.write(0,1,'Survived')
i=1
while i<419:
    feuil1.write(i,0,y_pred_final[i-1,0])
    feuil1.write(i,1,y_pred_final[i-1,1])
    i+=1

book.save(path)
























