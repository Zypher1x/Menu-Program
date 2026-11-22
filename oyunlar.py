
import random

while True:
    print("╔════════════════════════════════╗")
    print("║            OYUNLAR             ║")
    print("╠════════════════════════════════╣")
    print("║   1-Sayı Tahmin                ║")
    print("║   2-Adam Asmaca                ║")
    print("║   3-Taş Kağıt Makas            ║")
    print("║   4-Blackjack (21)             ║")
    print("║   6-Geri/Ana Menü              ║")
    print("╚════════════════════════════════╝")

    seçim = input("Seçiminizi Giriniz: ")

    if seçim == "1":
        sayı = random.randint(1, 100)
        hak = 7

        while hak > 0:
            tahmin = int(input("1-100 arasında sayı tahmin et: "))

            if tahmin == sayı:
                print("Tebrikler! Doğru bildin.")
                break

            elif tahmin < sayı:
                print("Daha büyük bir sayı!")

            else:
                print("Daha küçük bir sayı!")

            hak -= 1
            print("Kalan hak:", hak)

        if hak == 0:
            print("Kaybettin! Sayı:", sayı)

    elif seçim == "2":
        kelimeler = ["python", "bilgisayar", "yazilim", "oyun", "programlama"]
        kelime = random.choice(kelimeler)
        tahminler = []
        hak = 6

        while hak > 0:
            gösterim = ""

            for harf in kelime:
                if harf in tahminler:
                    gösterim += harf + " "
                else:
                    gösterim += "_ "

            print("\nKelime:", gösterim)
            print("Kalan hak:", hak)

            if all(harf in tahminler for harf in kelime):
                print("Tebrikler! Kazandın.")
                break

            tahmin = input("Bir harf gir: ").lower()

            if len(tahmin) != 1 or not tahmin.isalpha():
                print("Tek bir harf girmelisin!")
                continue

            if tahmin in tahminler:
                print("Bu harfi zaten denedin!")
                continue

            tahminler.append(tahmin)

            if tahmin not in kelime:
                hak -= 1
                print("Yanlış tahmin!")

        if hak == 0:
            print("Kaybettin! Kelime:", kelime)

    elif seçim == "3":
        seçenekler = ["taş", "kağıt", "makas"]
        bilgisayar = random.choice(seçenekler)

        oyuncu = input("Taş, kağıt veya makas: ").lower()

        if oyuncu not in seçenekler:
            print("Geçersiz seçim!")

        else:
            print("Bilgisayar:", bilgisayar)

            if oyuncu == bilgisayar:
                print("Berabere!")

            elif (oyuncu == "taş" and bilgisayar == "makas") or \
                 (oyuncu == "kağıt" and bilgisayar == "taş") or \
                 (oyuncu == "makas" and bilgisayar == "kağıt"):
                print("Kazandın!")

            else:
                print("Kaybettin!")

    elif seçim == "4":
        deste = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        oyuncu = [random.choice(deste), random.choice(deste)]
        bilgisayar = [random.choice(deste), random.choice(deste)]

        while sum(oyuncu) > 21 and 11 in oyuncu:
            oyuncu[oyuncu.index(11)] = 1

        while sum(bilgisayar) > 21 and 11 in bilgisayar:
            bilgisayar[bilgisayar.index(11)] = 1

        print("Senin kartların:", oyuncu)
        print("Toplam:", sum(oyuncu))
        print("Bilgisayarın açık kartı:", bilgisayar[0])

        while sum(oyuncu) < 21:
            işlem = input("Kart çek (k) / Dur (d): ").lower()

            if işlem == "k":
                kart = random.choice(deste)
                oyuncu.append(kart)

                if sum(oyuncu) > 21 and 11 in oyuncu:
                    oyuncu[oyuncu.index(11)] = 1

                print("Yeni kartların:", oyuncu)
                print("Toplam:", sum(oyuncu))

            elif işlem == "d":
                break

            else:
                print("Geçersiz seçim!")

        if sum(oyuncu) <= 21:
            while sum(bilgisayar) < 17:
                kart = random.choice(deste)
                bilgisayar.append(kart)

                if sum(bilgisayar) > 21 and 11 in bilgisayar:
                    bilgisayar[bilgisayar.index(11)] = 1

        print("\nSenin toplamın:", sum(oyuncu))
        print("Bilgisayarın kartları:", bilgisayar)
        print("Bilgisayarın toplamı:", sum(bilgisayar))

        if sum(oyuncu) > 21:
            print("Yandın! Bilgisayar kazandı.")

        elif sum(bilgisayar) > 21:
            print("Bilgisayar yandı! Kazandın.")

        elif sum(oyuncu) > sum(bilgisayar):
            print("Kazandın!")

        elif sum(oyuncu) < sum(bilgisayar):
            print("Kaybettin!")

        else:
            print("Berabere!")

    elif seçim == "6":
        print("Ana menüye dönülüyor...")
        import ana_menü
        break

    else:
        print("Geçersiz seçim!")