# 📊 Veri Bilimi ve Yapay Zekâ Projeleri

Veri bilimi ve yapay zekâ eğitimim boyunca tamamladığım projeler. Her klasörde Jupyter defteri, kullanılan veri (lisansı ve boyutu uygun olanlar) ve kısa bir açıklama bulunur.

**Sibel Er** · [LinkedIn](https://www.linkedin.com/in/sibel-e-b8166b162) · [Kaggle](https://www.kaggle.com/sibeler) · [Hugging Face](https://huggingface.co/Sibeller) · [Kişisel web sitem](https://ser2025.github.io/)

## Projeler

| # | Proje | Konu | Öne çıkan sonuç | Bağlantılar |
|---|---|---|---|---|
| 01 | [Titanic Hayatta Kalma Tahmini](01-titanik-makine-ogrenmesi) | Sınıflandırma (ML) | Doğrulama doğruluğu %83,8 | [Kaggle](https://www.kaggle.com/code/sibeler/titanic-hayatta-kalma-tahmini-eda-ve-ml-83-8) |
| 02 | [Dizüstü Bilgisayar Fiyat Tahmini](02-laptop-fiyat-tahmini) | Regresyon | R² 0,844 | |
| 03 | [Ülkelerin Askerî Güç Kümelemesi](03-askeri-guc-kumeleme) | Kümeleme (K-Means) | Silhouette 0,841 | |
| 04 | [Kredi Geri Ödeme Tahmini](04-kredi-geri-odeme-tahmini) | Sınıflandırma, veri temizliği | En güvenli %30'da geri ödeme %87,9 | [Kaggle](https://www.kaggle.com/code/sibeler/kredi-riski-veri-temizli-i-ve-s-n-fland-rma) |
| 05 | [Titanic: Keras ile Derin Öğrenme](05-titanic-keras-derin-ogrenme) | Derin öğrenme | Test accuracy ~%82,7 | |
| 06 | [Beton Basınç Dayanımı](06-beton-dayanimi-ann) | Regresyon + sınıflandırma, ANN | XGBoost R² 0,917 | [Kaggle](https://www.kaggle.com/code/sibeler/beton-bas-n-dayan-m-ml-ve-keras-r-0-917) |
| 07 | [CIFAR-10 Görüntü Sınıflandırma](07-cifar10-cnn) | CNN | Test accuracy ~%80,7 | |
| 08 | [GTSRB Trafik İşareti (Capstone)](08-gtsrb-trafik-isareti-cnn) | CNN | Test accuracy ~%96,0 | [Kaggle](https://www.kaggle.com/code/sibeler/gtsrb-trafik-areti-tan-ma-cnn-96-test) · [Model](https://huggingface.co/Sibeller/gtsrb-traffic-sign-cnn) |
| 09 | [İstanbul Kira Fiyatı Tahmini](09-istanbul-kira-tahmini) | Regresyon, ML + derin öğrenme | XGBoost R² 0,813 | [Kaggle](https://www.kaggle.com/code/sibeler/stanbul-kira-tahmini-xgboost-ve-keras) |
| 10 | [SMS Spam Dedektörü](10-sms-spam-dedektoru) | NLP + Streamlit uygulaması | Accuracy %98,3 | [Kaggle](https://www.kaggle.com/code/sibeler/sms-spam-tespiti-nlp-ile-98-do-ruluk) |

### Diğer projelerim

| Proje | Açıklama | Bağlantılar |
|---|---|---|
| [👗 Fashion Recommendation System](https://github.com/ser2025/fashion-recommendation-system) | Fotoğraftan görsel olarak benzer moda ürünlerini öneren sistem (VGG16, transfer learning) | [Canlı demo](https://sibel-fashion-recommendation.streamlit.app/) · [Veri seti](https://huggingface.co/datasets/Sibeller/fashion-data) |

## Kullanılan araçlar
`Python` · `pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `scikit-learn` · `XGBoost` · `TensorFlow / Keras` · `Streamlit` · `Jupyter`

## Çalıştırma
Her defter kendi klasöründeki veriyle çalışacak şekilde düzenlenmiştir:

```bash
git clone https://github.com/ser2025/veri-bilimi-projeleri.git
cd veri-bilimi-projeleri
jupyter notebook
```

Kredi (04), GTSRB (08) ve İstanbul kira (09) projelerinin verileri boyut nedeniyle depoya eklenmemiştir; kaynakları ilgili klasörün README dosyasında belirtilmiştir.
