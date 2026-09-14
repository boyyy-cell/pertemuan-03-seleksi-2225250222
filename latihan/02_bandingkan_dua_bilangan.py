bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

if bilangan1 >= bilangan2:
    if bilangan1 == bilangan2:
        print("Kedua bilangan sama.")
    else:
        print("Bilangan pertama lebih besar.")
else:
    print("Bilangan pertama lebih kecil.")