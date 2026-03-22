from sifre_olusturucu import sifre_uret, passphrase_uret


def baslik(metin):
    print(f"\n{'=' * 60}")
    print(f"  {metin}")
    print(f"{'=' * 60}\n")


def ornek(aciklama, sifre):
    print(f"→ {aciklama}")
    print(f"  {sifre}")
    print()


baslik("TEMEL ŞIFRE ÖRNEKLERİ")

ornek(
    "Varsayılan şifre (12 karakter)",
    sifre_uret()
)

ornek(
    "Kısa şifre (8 karakter)",
    sifre_uret(uzunluk=8)
)

ornek(
    "Orta şifre (16 karakter)",
    sifre_uret(uzunluk=16)
)

ornek(
    "Uzun şifre (32 karakter)",
    sifre_uret(uzunluk=32)
)

ornek(
    "Çok uzun şifre (50 karakter)",
    sifre_uret(uzunluk=50)
)


baslik("ÖZEL KARAKTER SETLERİ")

ornek(
    "Sadece harf ve rakam (özel karakter yok)",
    sifre_uret(uzunluk=16, ozel_karakter=False)
)

ornek(
    "Sadece büyük harf ve rakam",
    sifre_uret(uzunluk=12, kucuk_harf=False, ozel_karakter=False)
)

ornek(
    "Sadece küçük harf ve rakam",
    sifre_uret(uzunluk=12, buyuk_harf=False, ozel_karakter=False)
)

ornek(
    "Sadece harfler (rakam ve özel karakter yok)",
    sifre_uret(uzunluk=16, rakam=False, ozel_karakter=False)
)

ornek(
    "Sadece rakamlar (PIN kodu, 6 haneli)",
    sifre_uret(uzunluk=6, buyuk_harf=False, kucuk_harf=False, ozel_karakter=False)
)

ornek(
    "Uzun PIN kodu (12 haneli)",
    sifre_uret(uzunluk=12, buyuk_harf=False, kucuk_harf=False, ozel_karakter=False)
)


baslik("HATIRLANABİLİR ŞİFRELER (PASSPHRASE)")

ornek(
    "Varsayılan passphrase (4 kelime)",
    passphrase_uret()
)

ornek(
    "Kısa passphrase (3 kelime)",
    passphrase_uret(kelime_sayisi=3)
)

ornek(
    "Uzun passphrase (6 kelime)",
    passphrase_uret(kelime_sayisi=6)
)

ornek(
    "Çok uzun passphrase (8 kelime)",
    passphrase_uret(kelime_sayisi=8)
)

ornek(
    "Alt çizgi ayraçlı passphrase",
    passphrase_uret(kelime_sayisi=4, ayrac="_")
)

ornek(
    "Nokta ayraçlı passphrase",
    passphrase_uret(kelime_sayisi=5, ayrac=".")
)

ornek(
    "Boşluk ayraçlı passphrase (cümle gibi)",
    passphrase_uret(kelime_sayisi=5, ayrac=" ")
)


baslik("KULLANIM SENARYOLARı")

print("→ Web sitesi şifresi (orta güvenlik)")
for _ in range(3):
    print(f"  {sifre_uret(uzunluk=14)}")
print()

print("→ Banka/finansal şifre (yüksek güvenlik)")
for _ in range(3):
    print(f"  {sifre_uret(uzunluk=20)}")
print()

print("→ Wi-Fi şifresi (kolay paylaşılabilir)")
for _ in range(3):
    print(f"  {sifre_uret(uzunluk=16, ozel_karakter=False)}")
print()

print("→ Akılda kalıcı şifreler (passphrase)")
for _ in range(3):
    print(f"  {passphrase_uret(kelime_sayisi=4)}")
print()

print(f"{'=' * 60}\n")
print("💡 İpucu: Önemli hesaplar için en az 16 karakter kullanın!")
print("💡 İpucu: Passphrase'ler uzun ama kolay hatırlanır.")
print("💡 İpucu: Her hesap için farklı şifre kullanın.\n")
