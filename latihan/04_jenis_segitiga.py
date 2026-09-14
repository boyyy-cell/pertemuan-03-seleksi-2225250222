sisi1 = float(input("Masukkan sisi pertama: "))
sisi2 = float(input("Masukkan sisi kedua: "))
sisi3 = float(input("Masukkan sisi ketiga: "))

if sisi1 > 0 and sisi2 > 0 and sisi3 > 0:
    if sisi1 + sisi2 > sisi3 and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1:
        if sisi1 == sisi2:
            if sisi2 == sisi3:
                print("Segitiga sama sisi.")
            else:
                print("Segitiga sama kaki.")
        else:
            if sisi1 == sisi3 or sisi2 == sisi3:
                print("Segitiga sama kaki.")
            else:
                print("Segitiga sembarang.")
    else:
        print("Bukan segitiga.")
else:
    print("Bukan segitiga.")