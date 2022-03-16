from base_path import PROJECT_PATH
import wikipediaapi
import os
import re

print('imported')

wiki_wiki = wikipediaapi.Wikipedia(
        language='tr',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

topic_list = ['asal sayılar' , 'doğal sayılar', 
'karmaşık sayılar', 'toplama', 'çarpma', 'kümeler', 'modüler aritmetik', 
'apsis ve ordinat', 'birim fonksiyon', 'birim vektör', 
'eğim', 'fonksiyon', 'karekök', 'sayı doğrusu' ,
'rasyonel sayılar', 'reel sayılar', 'sabit fonksiyon', 
'sanal sayılar', 'geometrik seri', 'orantı', 'trigonometrik fonksiyonlar',
'ters trigonometrik fonksiyonlar', 'altın oran', 
'pi sayısı', 'çember', 'birim çember', 'çevre açı', 'çevrel çember',
'yarıçap', 'yay (geometri)', 'bileşik sayı', 'kare (cebir)', 'küp (cebir)',
'asal çarpan', 'asal çarpanlara ayırma', 'öklid teoremi', 'yarı asal',
'bölme', 'denk kesir', 'negatif sayı', 'tam kare', 'bölünebilme kuralları',
'kalan', 'kalanlı bölme', 'ortak bölen', 'ortak kat', 'polinom bölme',
'çıkarma', 'iki tam kare sayının farkı', 'kesir', 'yüzdelik', 'ağırlık merkezi',
'birleşme özelliği (ikili işlemler)', 'cebirsel ifade', 'çarpanlara ayırma',
'dağılma özelliği', 'denklem', 'doğrusal denklem', 'eşitsizlikler', 
'geçişlilik (matematik)', 'ikinci dereceden denklemler', 'işaret (matematik)',
'temel cebir', 'toplamaya göre ters', 'Birinci dereceden bir bilinmeyenli denklemler',
'denklem çözme', 'üçüncü dereceden denklemler', 'bütünler açılar', 'dik', 'dik açı',
'doğru parçası', 'hipotenüs', 'Kenar (geometri)', 'Kenarortay', 'Kesit', 'Merkez (geometri)',
'Nokta (geometri)', 'çevre açı', 'dış açı teoremi', 'kosinüs teoremi', 
'Öklid geometrisi', 'küre', 'birim küre', 'Paralel', 'Teğet', 'altıgen', 'üçgen', 'dörtgen', 
'beşgen', 'altıgen', 'yedigen', 'sekizgen', 'Tümler açılar', 'deltoid (geometri)', 'kare',
'daire', 'dikdörtgen', 'silindir', 'geometrik şekil', 'koni', 'alan', 'asimetri', 
'benzerlik (geometri)', 'beşgen prizma', 'çevre (geometri)', 'doğru (geometri)', 'doğru parçası',
'düzlem', 'eğri', 'eşkenar üçgen', 'ikizkenar üçgen', 'ikizkenar yamuk', 'kare piramit', 
'kartezyen koordinat sistemi', 'küp', 'Kenar (geometri)',
'Kesen', 'Örüntü', 'Parabol',
'Paralel',
'Paralelkenar', 'Piramit (geometri)',
'Pisagor üçlüsü', 'Prizma (geometri)',
'Tanjant', 'teğet', 'yamuk', 'devirli sayı', 'Determinant', 
'Kesit', 'De Morgan yasası',
'Kotanjant', 'üs', 'üstel fonksiyon', 
'Köşegen', 'Nokta (geometri)',
'Normal (geometri)', 'alt küme', 'ardışık sayılar', 'Bileşke fonksiyon',
'Birebir fonksiyon',
'Birebir örten fonksiyon',
'Birim fonksiyon', 'Örten fonksiyon', 'Sabit fonksiyon', 'Ters fonksiyon', 'sayı', 'açıortay',
]

file_path = os.path.dirname(__file__)
full_path = os.path.join(PROJECT_PATH, "files", "input_wiki_txt", "wiki_texts.txt")

with open(full_path, 'w', encoding='utf-8') as f:
    print('file created')


for topic in topic_list:
    page = wiki_wiki.page(topic)
    print(topic, ": " , page.exists())

    if page.exists():
        with open(full_path, 'a', encoding='utf-8') as f:
            string = " ".join(re.split("\s+", page.text, flags=re.UNICODE))
            string = string.lower()
            string = re.sub(r'(\\+)[a-z]*', '', string)
            string = string.translate(str.maketrans('', '', "()\{\}[]=+-.,?!"))
            string = string.split('ayrıca bakınız')[0].split('kaynakça')[0]
            f.write(string + "\n")






