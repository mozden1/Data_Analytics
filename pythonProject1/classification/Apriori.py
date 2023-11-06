from mlxtend.frequent_patterns import apriori
import pandas as pd

# Veri kümesini oluştur

df = pd.read_csv("sepet.csv")

# Ürünlerin listesini dönüştür
df['products'] = df['products'].apply(lambda x: ','.join(x))

# Apriori ile sıkça bir arada geçen öğeleri bul
frequent_itemsets: object = apriori(df['products'].str.get_dummies(sep=','), min_support=0.4, use_colnames=True)

# Bulguları görüntüle
print(frequent_itemsets)
