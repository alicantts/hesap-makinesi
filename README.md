# Hesap Makinesi

Python ile yazılmış, terminalde çalışan basit bir hesap makinesi.


## Özellikler

- Toplama, çıkarma, çarpma ve bölme
- Sıfıra bölmede uyarı mesajı
- Geçersiz işlem girilirse uyarı ve yeniden sorma
- Sonuçlar iki ondalık basamakla gösterilir
- `q` yazarak çıkış

## Gereksinimler

- Python 3.6 veya üzeri


## Kurulum ve çalıştırma

```
git clone https://github.com/alicantts/hesap-makinesi.git
cd hesap-makinesi
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Örnek kullanım

```
Islem (+, -, *, /) ya da q ile cik: +
1.Sayi: 0.1
2.Sayi: 0.2
Sonuc: 0.30
Islem (+, -, *, /) ya da q ile cik: /
1.Sayi: 8
2.Sayi: 0
Tanimsiz: sifira bolunemez
Islem (+, -, *, /) ya da q ile cik: q
Cikis Yapildi.
```

## Dosyalar

- `hesaplamalar.py`: dört işlemin fonksiyonları (`toplama`, `cikarma`, `carpma`, `bolme`).
  Fonksiyonlar yalnızca hesap yapar ve sonucu döndürür. Sıfıra bölmede `None` döner.
- `main.py`: kullanıcıdan veri alan ve sonucu yazdıran ana program.

## Bilinen sınırlamalar

- Sayı yerine harf girilirse program `ValueError` ile kapanır.
- `0` ile negatif bir sayının çarpımı `-0.00` olarak görünebilir (ondalık sayı gösteriminden kaynaklanan kozmetik bir durum).

