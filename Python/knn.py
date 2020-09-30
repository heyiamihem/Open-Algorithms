import numpy as np
from scipy.spatial import distance
from scipy import stats

def knnone(x_train,y_train,x_test,k=5):
    score=[]
    for loop in zip(x_train,y_train):
        score.append([distance.euclidean(x_test,loop[0]),loop[1]])
    score.sort(key = lambda x : x[0])
    score = np.array(score)
    return int(stats.mode(score[:k,1])[0])    

def knn(xtrain, ytrain, k=5):
  pred = []
  for x in xtest:
      pred.append(knn(xtrain,ytrain,x,k=5))
  return np.array(pred)
      
pred = knn(x,y,k)
