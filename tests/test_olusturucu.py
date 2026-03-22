import pytest
from sifre_olusturucu import sifre_uret, passphrase_uret


def test_varsayilan_sifre():
    sifre = sifre_uret()
    assert len(sifre) == 12
    assert isinstance(sifre, str)


def test_ozel_uzunluk():
    sifre = sifre_uret(uzunluk=20)
    assert len(sifre) == 20


def test_sadece_rakam():
    sifre = sifre_uret(
        buyuk_harf=False,
        kucuk_harf=False,
        rakam=True,
        ozel_karakter=False
    )
    assert sifre.isdigit()


def test_hatali_uzunluk():
    with pytest.raises(ValueError):
        sifre_uret(uzunluk=0)


def test_karakter_turu_yok():
    with pytest.raises(ValueError):
        sifre_uret(
            buyuk_harf=False,
            kucuk_harf=False,
            rakam=False,
            ozel_karakter=False
        )


def test_passphrase_varsayilan():
    passphrase = passphrase_uret()
    kelimeler = passphrase.split("-")
    assert len(kelimeler) == 4


def test_passphrase_ozel_kelime_sayisi():
    passphrase = passphrase_uret(kelime_sayisi=6)
    kelimeler = passphrase.split("-")
    assert len(kelimeler) == 6


def test_passphrase_ozel_ayrac():
    passphrase = passphrase_uret(ayrac="_")
    assert "_" in passphrase
    assert "-" not in passphrase


def test_passphrase_hatali_kelime_sayisi():
    with pytest.raises(ValueError):
        passphrase_uret(kelime_sayisi=0)


def test_uretilen_sifreler_farkli():
    sifre1 = sifre_uret()
    sifre2 = sifre_uret()
    assert sifre1 != sifre2
