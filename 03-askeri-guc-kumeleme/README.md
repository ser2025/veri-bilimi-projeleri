# 🌍 Ülkelerin Askerî Güçlerine Göre Kümelenmesi (K-Means)

138 ülke ve 60 özellikten oluşan veriyle ülkeleri askerî güç özelliklerine göre gruplandıran kümeleme projesi.

**Defter:** [`World_Military_Clustering.ipynb`](World_Military_Clustering.ipynb)

## Yöntem
StandardScaler, eksik veri stratejisi karşılaştırması (0 ile doldurma ve medyan), Elbow yöntemi, Silhouette skoru, 3 ve 4 kümeli modellerin karşılaştırılması.

## Sonuç
3 kümeli model Silhouette **0,841**. ABD, Çin-Rusya ve diğer ülkeler ayrı kümelere ayrıldı. 4 kümeli modelde Türkiye'nin de bulunduğu 24 ülkelik yüksek askerî güç grubu oluştu.

## Veri
`World military power.xlsx`

---
[← Tüm projeler](../README.md)
