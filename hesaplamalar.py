
while True:
    print("╔════════════════════════════════╗")
    print("║          HESAPLAMALAR          ║")
    print("╠════════════════════════════════╣")
    print("║   1-Toplama                    ║")
    print("║   2-Çıkarma                    ║")
    print("║   3-Bölme                      ║")
    print("║   4-Çarpma                     ║")
    print("║   5-Üssü Alma                  ║")
    print("║   6-Geri/Ana Menü              ║")
    print("╚════════════════════════════════╝")

    seçim = input("Seçiminizi Giriniz: ")

    if seçim == "1":
        sayı1 = float(input("Birinci sayı: "))
        sayı2 = float(input("İkinci sayı: "))
        print("Sonuç:", sayı1 + sayı2)

    elif seçim == "2":
        sayı1 = float(input("Birinci sayı: "))
        sayı2 = float(input("İkinci sayı: "))
        print("Sonuç:", sayı1 - sayı2)

    elif seçim == "3":
        sayı1 = float(input("Birinci sayı: "))
        sayı2 = float(input("İkinci sayı: "))

        if sayı2 == 0:
            print("Sıfıra bölme yapılamaz!")
        else:
            print("Sonuç:", sayı1 / sayı2)

    elif seçim == "4":
        sayı1 = float(input("Birinci sayı: "))
        sayı2 = float(input("İkinci sayı: "))
        print("Sonuç:", sayı1 * sayı2)

    elif seçim == "5":
        sayı1 = float(input("Taban: "))
        sayı2 = float(input("Üs: "))
        print("Sonuç:", sayı1 ** sayı2)

    elif seçim == "6":
        print("Çıkış yapılıyor...")
        import ana_menü
        break

    else:
        print("Geçersiz seçim!")