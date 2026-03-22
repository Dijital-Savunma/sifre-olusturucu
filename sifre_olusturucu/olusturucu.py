import secrets
import string


def sifre_uret(
    uzunluk=12,
    buyuk_harf=True,
    kucuk_harf=True,
    rakam=True,
    ozel_karakter=True
):
    karakterler = ""

    if buyuk_harf:
        karakterler += string.ascii_uppercase
    if kucuk_harf:
        karakterler += string.ascii_lowercase
    if rakam:
        karakterler += string.digits
    if ozel_karakter:
        karakterler += "!@#$%^&*()-_=+[]{}|;:,.<>?"

    if not karakterler:
        raise ValueError("En az bir karakter türü seçilmeli")

    if uzunluk < 1:
        raise ValueError("Şifre uzunluğu en az 1 olmalı")

    return "".join(secrets.choice(karakterler) for _ in range(uzunluk))


def passphrase_uret(kelime_sayisi=4, ayrac="-"):
    kelimeler = [
        "agac", "akar", "aslan", "ayak", "bahce", "balik", "beyaz", "bulut",
        "canak", "cicek", "deniz", "dikey", "duvar", "elma", "gecit", "gunes",
        "hamsi", "hizli", "insan", "kalem", "kapak", "kaplan", "kayik", "kedi",
        "kolay", "kopek", "kuslar", "mavi", "moral", "orman", "panda", "pencere",
        "renk", "sabah", "sakin", "sizma", "sokak", "susan", "tabak", "tarak",
        "tepsi", "tutam", "ucurum", "uzman", "vahsi", "yakit", "yesil", "yunus"
    ]

    if kelime_sayisi < 1:
        raise ValueError("Kelime sayısı en az 1 olmalı")

    secilen = [secrets.choice(kelimeler) for _ in range(kelime_sayisi)]
    return ayrac.join(secilen)
