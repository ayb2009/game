import random

def tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misiniz?")

    # Bilgisayarın rastgele bir sayı tutması
    gizli_sayi = random.randint(1, 100)
    tahmin_hakki = 10

    while tahmin_hakki > 0:
        # Kullanıcıdan tahmin al
        try:
            tahmin = int(input("Tahmininizi girin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        # Tahmini kontrol et
        if tahmin < gizli_sayi:
            print("Daha büyük bir sayı deneyin.")
        elif tahmin > gizli_sayi:
            print("Daha küçük bir sayı deneyin.")
        else:
            print(f"Tebrikler! {gizli_sayi} sayısını doğru tahmin ettiniz!")
            break

        tahmin_hakki -= 1
        print(f"Kalan tahmin hakkınız: {tahmin_hakki}")

    if tahmin_hakki == 0:
        print(f"Üzgünüm, tahmin hakkınız bitti. Doğru sayı {gizli_sayi} idi.")

if __name__ == "__main__":
    tahmin_oyunu()
