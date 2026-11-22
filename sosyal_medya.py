import webbrowser

while True:
    print("╔════════════════════════════════╗")
    print("║         SOSYAL MEDYA           ║")
    print("╠════════════════════════════════╣")
    print("║   1-Instagram                  ║")
    print("║   2-TikTok                     ║")
    print("║   3-X (Twitter)                ║")
    print("║   4-GitHub                     ║")
    print("║   5-Reddit                     ║")
    print("║   6-Geri/Ana Menü              ║")
    print("╚════════════════════════════════╝")

    seçim = input("Seçiminizi Giriniz: ")

    if seçim == "1":
        webbrowser.open("https://www.instagram.com")

    elif seçim == "2":
        webbrowser.open("https://www.tiktok.com")

    elif seçim == "3":
        webbrowser.open("https://x.com")

    elif seçim == "4":
        webbrowser.open("https://github.com")

    elif seçim == "5":
        webbrowser.open("https://www.reddit.com")

    elif seçim == "6":
        print("Ana menüye dönülüyor...")
        import ana_menü
        break

    else:
        print("Geçersiz seçim!")