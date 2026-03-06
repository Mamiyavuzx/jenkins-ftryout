def toplama(a, b):
    return a + b

sonuc = toplama(10, 20)
print(f"Deney Sonucu: {sonuc}")

# BİLEREK HATA YAPIYORUZ: 10+20 asla 35 etmez!
if sonuc != 35: 
    print("HATA: Matematiksel tutarsizlik tespit edildi!")
    exit(1) # Jenkins bu '1' kodunu gördüğü an build'i durdurur.
else:
    exit(0)
