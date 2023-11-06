from collections import defaultdict

# Veri Seti
sepetler = [
    ["elma", "muz", "üzüm"],
    ["elma", "üzüm"],
    ["muz", "portakal"],
    ["elma", "muz", "üzüm"],
    ["muz", "üzüm"]
]

# Minimum Destek Sayısı
min_destek = 2

# Öğe sıklıklarını hesapla
item_counts = defaultdict(int)

for sepet in sepetler:
    for item in sepet:
        item_counts[item] += 1

# Minimum destek kriterine göre geçerli öğeleri filtrele
valid_items = {item: count for item, count in item_counts.items() if count >= min_destek}

# Eşdeğerlik sınıflarını oluştur
equivalence_classes = {item: [] for item in valid_items}

for i, sepet in enumerate(sepetler):
    for item, count in valid_items.items():
        if sepet.count(item) == count:
            equivalence_classes[item].append(i + 1)

# Çapraz birleşimleri hesapla
cross_joins = {}

for item1 in valid_items:
    for item2 in valid_items:
        if item1 != item2:
            cross_join = list(set(equivalence_classes[item1]) & set(equivalence_classes[item2]))
            cross_joins[(item1, item2)] = cross_join

# Minimum destek kriterine göre geçerli çapraz birleşimleri filtrele
valid_cross_joins = {pair: sepetler for pair, sepetler in cross_joins.items() if len(sepetler) >= min_destek}

# Sonuçları yazdır
for (item1, item2), sepetler in valid_cross_joins.items():
    print(f"({item1}, {item2}) - Destek: {len(sepetler)}, Sepetler: {sepetler}")
