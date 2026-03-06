# Basit bir toplama deneyi
def toplama(a, b):
    return a + b

sonuc = toplama(10, 20)
print(f"Deney Sonucu: {sonuc}")

# Eger sonuc bekledigimiz gibi degilse sistem hata versin
if sonuc != 30:
    exit(1) # Hata kodu
else:
    exit(0) # Basari kodu
