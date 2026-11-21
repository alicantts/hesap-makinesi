from hesaplamalar import toplama, cikarma, carpma, bolme

while True:
    i = input("Islem (+, -, *, /) ya da q ile cik: ")

    if i == "q":
        print("Cikis Yapildi.")
        break

    if i not in ("+", "-", "*", "/"):
        print("Gecersiz islem girildi.")
        continue

    x = float(input("1.Sayi: "))
    y = float(input("2.Sayi: "))

    if i == "+":
        print(f"Sonuc: {toplama(x, y):.2f}")
    elif i == "-":
        print(f"Sonuc: {cikarma(x, y):.2f}")
    elif i == "*":
        print(f"Sonuc: {carpma(x, y):.2f}")
    elif i == "/":
        sonuc = bolme(x, y)
        if sonuc is None:
            print("Tanimsiz: sifira bolunemez")
        else:
            print(f"Sonuc: {sonuc:.2f}")
