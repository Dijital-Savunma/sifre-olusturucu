import argparse
import sys
from .olusturucu import sifre_uret, passphrase_uret


def main():
    parser = argparse.ArgumentParser(
        description='Güvenli şifre üretme aracı',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Örnekler:
  %(prog)s
  %(prog)s -u 14
  %(prog)s -u 15 --ozel-yok
  %(prog)s -p
  %(prog)s -p -k 6
  %(prog)s -a 5
        '''
    )

    parser.add_argument(
        '-u', '--uzunluk',
        type=int,
        default=12,
        help='Şifre uzunluğu (varsayılan: 12)'
    )

    parser.add_argument(
        '-p', '--passphrase',
        action='store_true',
        help='Passphrase (hatırlanabilir şifre) üret'
    )

    parser.add_argument(
        '-k', '--kelime-sayisi',
        type=int,
        default=4,
        help='Passphrase için kelime sayısı (varsayılan: 4)'
    )

    parser.add_argument(
        '-a', '--adet',
        type=int,
        default=1,
        help='Üretilecek şifre adedi (varsayılan: 1)'
    )

    parser.add_argument(
        '--buyuk-yok',
        action='store_true',
        help='Büyük harf kullanma'
    )

    parser.add_argument(
        '--kucuk-yok',
        action='store_true',
        help='Küçük harf kullanma'
    )

    parser.add_argument(
        '--rakam-yok',
        action='store_true',
        help='Rakam kullanma'
    )

    parser.add_argument(
        '--ozel-yok',
        action='store_true',
        help='Özel karakter kullanma'
    )

    args = parser.parse_args()

    try:
        for i in range(args.adet):
            if args.passphrase:
                sifre = passphrase_uret(kelime_sayisi=args.kelime_sayisi)
            else:
                sifre = sifre_uret(
                    uzunluk=args.uzunluk,
                    buyuk_harf=not args.buyuk_yok,
                    kucuk_harf=not args.kucuk_yok,
                    rakam=not args.rakam_yok,
                    ozel_karakter=not args.ozel_yok
                )
            print(sifre)
    except ValueError as e:
        print(f"Hata: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
