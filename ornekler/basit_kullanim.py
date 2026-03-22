from sifre_olusturucu import sifre_uret, passphrase_uret


print("=== Basit Şifre Örnekleri ===\n")

print("Varsayılan şifre (12 karakter):")
print(sifre_uret())
print()

print("Uzun şifre (24 karakter):")
print(sifre_uret(uzunluk=24))
print()

print("Sadece harf ve rakam (özel karakter yok):")
print(sifre_uret(ozel_karakter=False))
print()

print("Kısa PIN (sadece rakam, 6 haneli):")
print(sifre_uret(uzunluk=6, buyuk_harf=False, kucuk_harf=False, ozel_karakter=False))
print()

print("\n=== Passphrase Örnekleri ===\n")

print("Varsayılan passphrase (4 kelime):")
print(passphrase_uret())
print()

print("Uzun passphrase (6 kelime):")
print(passphrase_uret(kelime_sayisi=6))
print()

print("Alt çizgi ayraçlı:")
print(passphrase_uret(ayrac="_"))
print()
