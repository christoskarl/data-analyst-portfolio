
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

data = {
    "CustomerID": [1, 2, 3, 4, 5],
    "Age": [25, 45, 35, 23, 40],
    "Annual Income (k$)": [30, 60, 45, 28, 55],
}
df = pd.DataFrame(data)

X = df[["Age", "Annual Income (k$)"]]
kmeans = KMeans(n_clusters=2, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Age", y="Annual Income (k$)", hue="Cluster", palette="Set2")
plt.title("Customer Segmentation")
plt.show()
