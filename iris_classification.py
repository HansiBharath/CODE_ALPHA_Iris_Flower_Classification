  
import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import LabelEncoder  
from sklearn.tree import DecisionTreeClassifier  
from sklearn.metrics import accuracy_score  

df = pd.read_csv("Iris.csv")  

label_encoder = LabelEncoder()  
df["Species"] = label_encoder.fit_transform(df["Species"])  

X = df.drop(columns=["Species"])  
y = df["Species"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

model = DecisionTreeClassifier()  
model.fit(X_train, y_train)  

y_pred = model.predict(X_test)  

accuracy = accuracy_score(y_test, y_pred)  
print(f"Model Accuracy: {accuracy * 100:.2f}%")  
