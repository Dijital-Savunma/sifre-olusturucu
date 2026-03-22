# Şifre Oluşturucu

Güvenli ve kullanımı kolay şifre üretme kütüphanesi.

---

## 🌐 Web Arayüzü

### [**Şimdi Dene - Tarayıcıda Şifre Üret**](https://dijitalsavunma.org/sifre-olusturucu)

Hiçbir şey kurmadan, doğrudan tarayıcınızda güvenli şifre oluşturun.

**Özellikler:**
- ✅ 6-50 karakter arası uzunluk seçimi
- ✅ Karakter türü kontrolleri (büyük/küçük harf, rakam, özel karakter)
- ✅ Tek tıkla kopyalama
- ✅ Modern, mobil uyumlu tasarım
- ✅ %100 client-side, hiçbir veri sunucuya gönderilmez

---

## 📦 Kurulum

```bash
pip install git+https://github.com/dijital-savunma/sifre-olusturucu.git
```

## 💻 Komut Satırından Kullanım (CLI)

Kurulumdan sonra `sifre-uret` komutu ile doğrudan kullanabilirsiniz:

```bash
sifre-uret                    # Varsayılan (12 karakter)
sifre-uret -u 14             # 14 haneli şifre
sifre-uret -u 15             # 15 haneli şifre
sifre-uret -u 18             # 18 haneli şifre
sifre-uret -u 16 --ozel-yok  # Özel karakter olmadan
sifre-uret -a 5              # 5 farklı şifre üret
sifre-uret -p                # Passphrase (hatırlanabilir)
sifre-uret -p -k 6           # 6 kelimelik passphrase
```

### Tüm Seçenekler

```bash
sifre-uret --help
```

**Parametreler:**
- `-u, --uzunluk`: Şifre uzunluğu (varsayılan: 12, maksimum sınır yok)
- `-p, --passphrase`: Hatırlanabilir şifre üret
- `-k, --kelime-sayisi`: Passphrase kelime sayısı (varsayılan: 4)
- `-a, --adet`: Üretilecek şifre adedi (varsayılan: 1)
- `--buyuk-yok`: Büyük harf kullanma
- `--kucuk-yok`: Küçük harf kullanma
- `--rakam-yok`: Rakam kullanma
- `--ozel-yok`: Özel karakter kullanma

## 🐍 Python Kodunda Kullanım

### Hızlı Başlangıç

```python
from sifre_olusturucu import sifre_uret

sifre = sifre_uret()
print(sifre)
```

### Özel Uzunlukta Şifre

```python
sifre_14 = sifre_uret(uzunluk=14)
sifre_15 = sifre_uret(uzunluk=15)
sifre_18 = sifre_uret(uzunluk=18)
```

### Belirli Karakter Türleriyle

```python
sifre = sifre_uret(
    uzunluk=16,
    buyuk_harf=True,
    kucuk_harf=True,
    rakam=True,
    ozel_karakter=False
)
```

### Hatırlanabilir Şifre (Passphrase)

```python
from sifre_olusturucu import passphrase_uret

sifre = passphrase_uret(kelime_sayisi=4)
```

## ✨ Özellikler

- 🔐 Python'un `secrets` modülü ile kriptografik güvenli rastgelelik
- 🎯 Basit ve anlaşılır API
- 💻 Komut satırı arayüzü (CLI)
- 🌐 Web arayüzü (dijitalsavunma.org)
- ⚙️ Özelleştirilebilir karakter setleri
- 🧠 Hatırlanabilir passphrase desteği
- 📏 İstediğiniz uzunlukta güçlü şifreler
- 📦 Sıfır dışa bağımlılık
- 🇹🇷 %100 Türkçe

## 🔒 Güvenlik

Bu kütüphane şifre üretimi için Python'un `secrets` modülünü kullanır. `random` modülünden farklı olarak `secrets`, kriptografik amaçlar için güvenlidir ve tahmin edilemez şifreler üretir.

Web arayüzü tamamen client-side çalışır. Hiçbir veri sunucuya gönderilmez, tarayıcınızın kriptografik API'si kullanılır.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull request göndermekten çekinmeyin.

- 🐛 Hata bildirimleri
- 💡 Yeni özellik önerileri
- 📝 Dokümantasyon iyileştirmeleri
- 🌐 Türkçe kelime listesi genişletmeleri

## 📄 Lisans

Apache License 2.0

---

**[Dijital Savunma](https://dijitalsavunma.org)** topluluğunun bir projesidir.
