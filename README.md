# Şifre Oluşturucu

Güvenli ve kullanımı kolay şifre üretme kütüphanesi.

---

## 🌐 Web Arayüzü

### [**Şimdi Dene - Tarayıcıda Şifre Üret**](https://raw.githack.com/dijital-savunma/sifre-olusturucu/main/index.html)

Hiçbir şey kurmadan, doğrudan tarayıcınızda güvenli şifre oluşturun.

**Özellikler:**
- ✅ 6-18 karakter arası uzunluk seçimi
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
- `-u, --uzunluk`: Şifre uzunluğu (6-18 arası önerilir, varsayılan: 12)
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

## 🚀 GitHub'da Kullanım

### Doğrudan Komut Satırında

```bash
git clone https://github.com/dijital-savunma/sifre-olusturucu.git
cd sifre-olusturucu
python3 -m sifre_olusturucu -u 14
```

### GitHub Actions ile

`.github/workflows/sifre-uret.yml` dosyası oluşturun:

```yaml
name: Şifre Üret

on:
  workflow_dispatch:

jobs:
  sifre-uret:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Python Kur
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Şifre Üret
        run: |
          python3 -m sifre_olusturucu -u 14
          python3 -m sifre_olusturucu -u 15
          python3 -m sifre_olusturucu -p
```

## ✨ Özellikler

- 🔐 Python'un `secrets` modülü ile kriptografik güvenli rastgelelik
- 🎯 Basit ve anlaşılır API
- 💻 Komut satırı arayüzü (CLI)
- 🌐 Web arayüzü (GitHub Pages)
- ⚙️ Özelleştirilebilir karakter setleri
- 🧠 Hatırlanabilir passphrase desteği
- 📏 6-18 haneli güçlü şifreler
- 📦 Sıfır dışa bağımlılık
- 🇹🇷 %100 Türkçe

## 🔒 Güvenlik

Bu kütüphane şifre üretimi için Python'un `secrets` modülünü kullanır. `random` modülünden farklı olarak `secrets`, kriptografik amaçlar için güvenlidir ve tahmin edilemez şifreler üretir.

Web arayüzü tamamen client-side çalışır. Hiçbir veri sunucuya gönderilmez, tarayıcınızın kriptografik API'si kullanılır.

## 🧪 Testler

```bash
pip install pytest
pytest tests/
```

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz. [CONTRIBUTING.md](https://github.com/dijital-savunma/topluluk/blob/main/CONTRIBUTING.md) dosyasına göz atın.

## 📄 Lisans

[Apache License 2.0](LICENSE)

---

**[Dijital Savunma](https://github.com/dijital-savunma/topluluk)** topluluğunun bir projesidir.
