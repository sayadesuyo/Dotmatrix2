import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df=pd.read_csv("Web顧客別データ.xlsx")

num_att=["年齢","前回購入からの日数"]
cat_att=["性別"]

cat_onehot=pd.get_dummies(df[cat_att],dtype=int)


X=pd.concat([df[num_att],cat_onehot],axis=1)
Y=df["休眠顧客化"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

model=DecisionTreeClassifier(max_depth=30,random_state=0)
#random_state=0　：　ランダムでも同じランダムになる

model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)


tn,fp,fn,tp=confusion_matrix(Y_test,Y_pred,labels=[False,True]).ravel()

accuracy=(tp+tn)/(tn+fp+fn+tp)

precision=tp/(tp+fp)

recall=tp/(tp+fn)

flscore=2*precision*recall/(precision+recall)