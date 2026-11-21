from hesaplamalar import toplama, cikarma, carpma, bolme

x = float(input("1.Sayi: "))
y = float(input("2.Sayi: "))
i = input("Işlem: ")

if i == "+":
    print("Sonuc:", toplama(x, y))
elif i == "-":
    print("Sonuc:", cikarma(x, y))
elif i == "*":
    print("Sonuc:", carpma(x, y))
elif i == "/":
    sonuc = bolme(x, y)
    if sonuc is None:
        print("Tanimsiz: sifira bolunemez")
    else:
        print(sonuc)
else:
    print("Gecersiz islem girildi.")
