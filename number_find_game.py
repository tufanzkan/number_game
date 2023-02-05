import random
import time

print("*** SAYI BULMA OYUNU(0,100) *** \n")

bulunacak=random.randint(0,100)

def oyun_baslat():
    global sayi
    sayi=int(input("bi sayi giriniz: "))
    return sayi

baslangic=time.time()
oyun_baslat()
while True:
    if sayi<bulunacak:
        print("kontrol ediliyor...")
        time.sleep(1)
        print("tahmininiz bulunacak sayinin altinda")
        oyun_baslat()
    elif sayi>bulunacak:
        print("kontrol ediliyor...")
        time.sleep(1)
        print("tahmininiz bulunacak sayinin ustunde")
        oyun_baslat()
    elif sayi==bulunacak:
        print("kontrol ediliyor...")
        time.sleep(1)
        print("dogru buldunuz TBERİKLERRR")
        global bitis
        bitis=time.time()
        break

gecensure=bitis - baslangic
print()
print(f"gecen sure: {int(gecensure)} saniye")