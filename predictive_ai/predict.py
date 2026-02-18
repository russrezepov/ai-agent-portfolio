import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import ollama

data = {
    "logins_per_week": [1,2,10,8,3,15,7,2],
    "tickets": [5,4,0,1,3,0,1,6],
    "usage_hours": [2,3,20,18,5,25,15,1],
    "churn": [1,1,0,0,1,0,0,1]
}

df = pd.DataFrame(data)
X = df.drop("churn", axis=1)
y = df["churn"]

model = RandomForestClassifier()
model.fit(X, y)

sample = X.iloc[[0]]
risk = model.predict_proba(sample)[0][1]

explanation = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": f"Explain why churn risk is {risk:.2f} for this customer:\n{sample.to_dict()}"}]
)
print(f"Churn risk: {risk:.2f}")
print(explanation["message"]["content"])
