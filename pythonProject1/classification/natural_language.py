import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# NLTK verilerini yükleyelim.
nltk.download('punkt')
nltk.download('stopwords')

# Metin verisi
metin = """
Doğal Dil İşleme (NLP), makine öğrenimi ve yapay zeka alanlarında bir alt dal olarak kabul edilir. 
Bu alandaki temel amaç, bilgisayarların insanların doğal dilini anlamasına ve işlemesine olanak sağlamaktır.
NLP, metin sınıflandırma, metin özetleme, duygu analizi ve otomatik cevaplandırma gibi birçok uygulama alanında kullanılır.
"""

# Metni cümlelerine bölelim.
cümleler = sent_tokenize(metin)

# Metni kelimelere bölelim ve gereksiz kelimeleri (stop words) çıkaralım.
stop_words = set(stopwords.words('turkish'))
kelimeler = word_tokenize(metin)
temiz_kelimeler = [kelime for kelime in kelimeler if kelime.lower() not in stop_words]

# Cümle sayısını ve kelime sayısını hesaplayalım.
cümle_sayısı = len(cümleler)
kelime_sayısı = len(temiz_kelimeler)

# Sonuçları yazdıralım.
print("Metindeki Cümle Sayısı:", cümle_sayısı)
print("Metindeki Toplam Kelime Sayısı:", kelime_sayısı)
print("Temizlenmiş Kelimeler:", temiz_kelimeler)
nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# NLTK verilerini yükleyelim.
nltk.download('punkt')
nltk.download('stopwords')

# Metin verisi
metin = """
Doğal Dil İşleme (NLP), makine öğrenimi ve yapay zeka alanlarında bir alt dal olarak kabul edilir. 
Bu alandaki temel amaç, bilgisayarların insanların doğal dilini anlamasına ve işlemesine olanak sağlamaktır.
NLP, metin sınıflandırma, metin özetleme, duygu analizi ve otomatik cevaplandırma gibi birçok uygulama alanında kullanılır.
"""

# Metni cümlelerine bölelim.
cümleler = sent_tokenize(metin)

# Metni kelimelere bölelim ve gereksiz kelimeleri (stop words) çıkaralım.
stop_words = set(stopwords.words('turkish'))
kelimeler = word_tokenize(metin)
temiz_kelimeler = [kelime for kelime in kelimeler if kelime.lower() not in stop_words]

# Cümle sayısını ve kelime sayısını hesaplayalım.
cümle_sayısı = len(cümleler)
kelime_sayısı = len(temiz_kelimeler)

# Sonuçları yazdıralım.
print("Metindeki Cümle Sayısı:", cümle_sayısı)
print("Metindeki Toplam Kelime Sayısı:", kelime_sayısı)
print("Temizlenmiş Kelimeler:", temiz_kelimeler)
