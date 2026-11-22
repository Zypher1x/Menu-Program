
import turtle

t = turtle.Turtle()
t.speed(5)

while True:
    print("╔════════════════════════════════╗")
    print("║            ÇİZİMLER            ║")
    print("╠════════════════════════════════╣")
    print("║   1-Kare                       ║")
    print("║   2-Üçgen                      ║")
    print("║   3-Dikdörtgen                 ║")
    print("║   4-Altıgen                    ║")
    print("║   5-Çiçek                      ║")
    print("║   6-Geri/Ana Menü              ║")
    print("╚════════════════════════════════╝")

    seçim = input("Seçiminizi Giriniz: ")

    t.clear()
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    if seçim == "1":
        for i in range(4):
            t.forward(100)
            t.right(90)

    elif seçim == "2":
        for i in range(3):
            t.forward(100)
            t.left(120)

    elif seçim == "3":
        for i in range(2):
            t.forward(150)
            t.right(90)
            t.forward(80)
            t.right(90)

    elif seçim == "4":
        for i in range(6):
            t.forward(100)
            t.right(60)

    elif seçim == "5":
        for i in range(12):
            t.speed(100)
            t.circle(50)
            t.right(30)

    elif seçim == "6":
        print("Ana menüye dönülüyor...")
        turtle.bye()
        import ana_menü
        break

    else:
        print("Geçersiz seçim!")
