#Kullanılacak kütüphanelerin içe aktarımı
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#Kullanılacak Verinin içe aktarımı
df=pd.read_csv("wine.csv")
x = df
#Verinin standardize edilmesi
std  = StandardScaler()
scaler_x=std.fit_transform(x)
#Algoritmanın yüklenmesi ve eğitimi
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(scaler_x)
df["küme"]=kmeans.labels_
#Sonucun alınması
print(df)
# Görselleştirme
plt.scatter(scaler_x[:, 0], scaler_x[:, 5], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Küme Merkezleri')
plt.xlabel('Alcohol')
plt.ylabel('Magnesium')
plt.title('şarap kümesi')
plt.legend()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Veri çerçevenizi ve alkol oranları gibi sayısal sütunları içeren bir örnek veri çerçevesini kullanalım.
# Ayrıca her bir öbeği temsil eden bir "Cluster" sütunu olduğunu varsayalım.

# Veri çerçevesini ve öbek sütununu yükleyin (veri adı ve Cluster adı olarak varsayalım).
# Ayrıca, sayısal sütunları bir liste içinde saklayın.
data = df
cluster_column = "küme"  # Öbek sütunu
numerical_columns = ["Alcohol", "Ash","Magnesium","Total_Phenols","Nonflavanoid_Phenols","Proanthocyanins","Color_Intensity"]  # Sayısal sütunlar

# Her sayısal sütun için ayrı kutu grafiği çizin.
for col in numerical_columns:
    plt.figure(figsize=(10, 6))  # Grafiğin boyutunu ayarlayın.
    sns.set(style="whitegrid")

    sns.boxplot(x=cluster_column, y=col, data=data)

    cluster_labels = data[cluster_column].unique()
    plt.xticks(range(len(cluster_labels)), cluster_labels)



    plt.title(f"{col} Sütunu Öbek (Küme) Bazında Kutu Grafiği")
    plt.xlabel("Öbek (Küme)")
    plt.ylabel(col)

    plt.show()


