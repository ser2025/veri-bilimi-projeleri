# SMS Spam Dedektörü (Streamlit)

Bir SMS'in spam olup olmadığını tahmin eden ve kararı hangi kelimelerin etkilediğini gösteren web uygulaması.

## Klasördeki dosyalar

| Dosya | Ne işe yarar? |
|---|---|
| `Ham_or_Spam.ipynb` | Veri analizi, temizlik, 3 modelin karşılaştırması; modeli eğitip `spam_model.pkl` olarak kaydeder |
| `spam.csv` | 5.572 SMS (Kaggle SMS Spam Collection) |
| `spam_model.pkl` | Kaydedilmiş model: CountVectorizer + Naive Bayes (Pipeline) |
| `app.py` | Streamlit uygulaması |
| `ornek_mesajlar.csv` | Toplu kontrol için 8 örnek mesaj |
| `requirements.txt` | Gerekli paketler |
| `.streamlit/config.toml` | Uygulamanın renk teması |
| `ekran_goruntuleri/` | Uygulamanın 3 ekran görüntüsü |

## Çalıştırma

```
pip install -r requirements.txt
streamlit run app.py
```

Tarayıcıda `http://localhost:8501` açılır. Telefonda denemek için aynı Wi-Fi'daki telefonun tarayıcısına terminalde yazan **Network URL** adresini yaz.

## Uygulamanın iki sekmesi

- **Tek mesaj:** Mesajı yapıştır; model spam / normal kararını ve spam olasılığını verir. Mesaj balonunda kırmızı işaretli kelimeler spam'e, yeşil işaretliler normal mesaja işaret eder. Altındaki tablo en etkili kelimeleri puanlarıyla gösterir.
- **Toplu kontrol (CSV):** `text` sütunu olan bir CSV yükle; her mesaj için tahmin ve olasılık çıkar, sonuçlar CSV olarak indirilir. Dosya yüklenmezse `ornek_mesajlar.csv` kullanılır.

## Kodun mantığı

1. **Model yükleme:** `joblib.load('spam_model.pkl')` notebook'ta eğitilen Pipeline'ı açar. İçinde hem kelime sözlüğü (`Vect`) hem model (`Classifier`) vardır.
2. **Kelime spam puanı:** Naive Bayes her kelimenin spam ve normal mesajlarda görülme olasılığını öğrenir (`feature_log_prob_`). İkisinin farkı kelimenin "spam puanı"dır: 0'dan büyükse spam'de, küçükse normal mesajda daha sık geçer. 1,5'in üstü (yaklaşık 4,5 kat daha sık) kırmızı, -1,5'in altı yeşil işaretlenir.
3. **Aynı temizlik:** `temizle` fonksiyonu notebook'taki adımların aynısıdır (küçük harf, gereksiz kelimeler, noktalama, özel karakterler). Yeni mesaj eğitimdekiyle aynı işlemden geçmezse model yanılır.
4. **`if` kullanmadan karar gösterme:** `{'spam':st.error,'ham':st.success}[karar](...)`: karar 'spam' ise kırmızı, 'ham' ise yeşil kutu seçilir.
5. **`if` kullanmadan dosya seçimi:** `st.file_uploader(...) or 'ornek_mesajlar.csv'`: dosya yüklenmezse örnek dosya okunur.
6. **Renkli işaretleme:** `np.where` her kelimeye puanına göre kırmızı, yeşil ya da düz biçim verir; döngü gerekmez.

## İnternete koymak (isteğe bağlı)

- **Streamlit Community Cloud:** Klasörü bir GitHub deposuna yükle, share.streamlit.io'da "New app" de, depoyu ve `app.py`'yi seç.
- **Hugging Face Spaces:** Yeni bir Space aç (SDK: Streamlit), klasördeki dosyaları yükle.
