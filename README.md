# 📊 Veri Bilimi ve Yapay Zekâ Projeleri

Veri bilimi ve yapay zekâ eğitimim boyunca tamamladığım projeler. Her klasörde Jupyter defteri, kullanılan veri (lisansı ve boyutu uygun olanlar) ve kısa bir açıklama bulunur.

**Sibel Er** · [GitHub](https://github.com/ser2025) · [Kaggle](https://www.kaggle.com/sibeler) · [Hugging Face](https://huggingface.co/Sibeller)

## Projeler

| # | Proje | Konu | Öne çıkan sonuç |
|---|---|---|---|
| 01 | [Titanic Hayatta Kalma Tahmini](01-titanik-makine-ogrenmesi) | Sınıflandırma (ML) | Doğrulama doğruluğu %83,8 |
| 02 | [Dizüstü Bilgisayar Fiyat Tahmini](02-laptop-fiyat-tahmini) | Regresyon | R² 0,844 |
| 03 | [Ülkelerin Askerî Güç Kümelemesi](03-askeri-guc-kumeleme) | Kümeleme (K-Means) | Silhouette 0,841 |
| 04 | [Kredi Geri Ödeme Tahmini](04-kredi-geri-odeme-tahmini) | Sınıflandırma, veri temizliği | En güvenli %30'da geri ödeme %87,9 |
| 05 | [Titanic: Keras ile Derin Öğrenme](05-titanic-keras-derin-ogrenme) | Derin öğrenme | Test accuracy ~%82,7 |
| 06 | [Beton Basınç Dayanımı](06-beton-dayanimi-ann) | Regresyon + sınıflandırma, ANN | XGBoost R² 0,917 |
| 07 | [CIFAR-10 Görüntü Sınıflandırma](07-cifar10-cnn) | CNN | Test accuracy ~%80,7 |
| 08 | [GTSRB Trafik İşareti (Capstone)](08-gtsrb-trafik-isareti-cnn) | CNN | Test accuracy ~%96,0 |
| 09 | [İstanbul Kira Fiyatı Tahmini](09-istanbul-kira-tahmini) | Regresyon, ML + derin öğrenme | XGBoost R² 0,813 |
| 10 | [SMS Spam Dedektörü](10-sms-spam-dedektoru) | NLP + Streamlit uygulaması | Accuracy %98,3 |

## Kullanılan araçlar
`Python` · `pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `scikit-learn` · `XGBoost` · `TensorFlow / Keras` · `Streamlit` · `Jupyter`

## Çalıştırma
Her defter kendi klasöründeki veriyle çalışacak şekilde düzenlenmiştir:

```bash
git clone https://github.com/ser2025/veri-bilimi-projeleri.git
cd veri-bilimi-projeleri
jupyter notebook
```
