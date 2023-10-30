def k_kucuk(sayi, liste):

    #Verilen bir listenin içindeki k. en küçük değeri bulan fonksiyon.
    
    liste.sort() 
    k_kucuk_sonuc = liste[sayi - 1] # Listedeki k. değer (k-1). indexte olacak.
    return k_kucuk_sonuc

def en_yakin_cift(sayi, liste):
    
    #Verilen bir sayıya en yakın toplamı veren liste elemanlarını bulan fonksiyon.

    liste.sort() 
    sol = 0 # Listenin en kücük elemaninin indexi
    sag = len(liste) - 1 # Listenin en büyük elemanının indexi
    en_yakin_cift_sonuc = None 
    min_fark = float('inf') 

    # Listeyi sağdan ve soldan ortaya doğru gezen bir döngü
    while sol < sag: 

        mevcut_toplam = liste[sol] + liste[sag] 
        mevcut_fark = abs(sayi - mevcut_toplam) 

        if mevcut_fark < min_fark: 
            min_fark = mevcut_fark 
            en_yakin_cift_sonuc = (liste[sol], liste[sag]) # En yakın çift sonuç güncellenir.

        if mevcut_toplam < sayi:
            sol += 1 
        else: 
            sag -= 1 

    return en_yakin_cift_sonuc # Döngü bittiğinde en yakın çift sonuç döndürülür.

def tekrar_eden_elemanlar(liste):
    
    #Verilen bir listedeki tekrar eden elemanları bulan fonksiyon.

    # Tekrar eden elemanlar listenin liste içerisinde sayısı 1'den büyük olan elemanlarıdır.
    tekrar_eden_elemanlar_sonuc = [x for x in liste if liste.count(x) > 1] 
    
    # set'e çevirerek tekrar edenlerden arındırıyoruz.
    tekrar_eden_elemanlar_sonuc = list(set(tekrar_eden_elemanlar_sonuc))
    
    return tekrar_eden_elemanlar_sonuc

def matris_carpimi(matris1, matris2):
    
    #İki matrisin çarpımını hesaplayan fonksiyon.
    
    if len(matris1[0]) != len(matris2):
        raise ValueError("Matris boyutları uyumsuz.")

    # İlk matrisin her satırını alıyoruz.
    matris_carpimi_sonuc = []

    for row in matris1:
        satir_sonuc = []

        # İkinci matrisin sütunlarını alıyoruz 
        for col in zip(*matris2):
            carpim = 0

            # Her elemanın çarpımını hesaplayıp topluyoruz.
            for a, b in zip(row, col):
                carpim += a * b

            satir_sonuc.append(carpim)

        matris_carpimi_sonuc.append(satir_sonuc)

    return matris_carpimi_sonuc


def kelime_frekansi(dosya_konumu):
    
    #Bir metin dosyasındaki kelimelerin frekansını bulan fonksiyon.
    
    kelime_frekanslari = {} 
    with open(dosya_konumu, 'r') as dosya: 
        kelimeler = dosya.read().split() 

    for kelime in kelimeler: 
        kelime = kelime.lower()  
        kelime_frekanslari[kelime] = kelime_frekanslari.get(kelime, 0) + 1 
                                                                             

    # Kelime frekanslarını azalan sırayla sıralıyoruz.
    sirali_kelime_frekanslari = dict(sorted(kelime_frekanslari.items(), key=lambda x: x[1], reverse=True))

    return sirali_kelime_frekanslari

def en_kucuk_deger(liste):
    
    #Bir listenin içindeki en küçük değeri özyinelemeli olarak bulan fonksiyon.
    
    if not liste:  
        return None

    if len(liste) == 1:  
        return liste[0]

    
    # Listenin ilk elemanı kalan_en_kucuk adlı değişkende saklanır.
    kalan_en_kucuk = en_kucuk_deger(liste[1:])


    return liste[0] if liste[0] < kalan_en_kucuk else kalan_en_kucuk

def karekok(N, x0, tol=1e-10, maxiter=10, iterasyon=0):
    
    #Bir sayının karekökünü hesaplayan özyinelemeli fonksiyon.
    
    if iterasyon > maxiter: 
        print(f"{maxiter} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin")
        return x0 
    
    
    xn = 0.5 * (x0 + N / x0)
    hata = abs(xn * xn - N)
    
    if hata < tol: 
        return xn
    else: 
        return karekok(N, xn, tol, maxiter, iterasyon + 1)

def eb_ortak_bolen(a, b):
    
    # İki sayının en büyük ortak bölenini hesaplayan fonksiyon.
    
    if b == 0: 
        return a
    return eb_ortak_bolen(b, a % b) 

def asal_veya_degil(sayi, bölen=2):
    
    #Bir sayının asal olup olmadığını kontrol eden özyinelemeli fonksiyon.
    
    if sayi <= 1: 
        return False
    if sayi == bölen: 
        return True
    if sayi % bölen == 0: # Eğer ki sayı bölene tam bölünebiliyorsa asal değildir.
        return False
    return asal_veya_degil(sayi, bölen + 1) # Bölen artırılarak 2'den sayi'ya kadar olan tüm sayılara bölünüp bölünemediği denenir.

def hizlandirici(n, k, fib_k, fib_k1):

    # Fibonacci dizisinin n. terimini hesaplayan özyinelemeli fonksiyon.
    
    if k == n: 
        return fib_k
    else:
        return hizlandirici(n, k + 1, fib_k + fib_k1, fib_k) 
    
def tam_sayi_listesi_inputu_al():
    
    # Kullanıcıdan boşlukla ayrılmış tam sayıların bir listesini girmesini isteyen fonksiyon.
    
    liste_input = input("Lütfen listeyi sayılar arasında boşluklar olacak şekilde giriniz: ") 
            
    string_listesi = liste_input.split(' ') 

    return [int(sayi) for sayi in string_listesi] 


def main():

    girilen_sayi = 0 # Kullanıcı tarafından girilen sayı.

    while(girilen_sayi != 11):
        
        print("1. k'ninci En Küçük Elemanı Bulma")
        print("2. En Yakın Çifti Bulma")
        print("3. Bir Listenin Tekrar Eden Elemanlarını Bulma")
        print("4. Matris Çarpımı")
        print("5. Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
        print("6. Liste İçinde En Küçük Değeri Bulma")
        print("7. Karekök Fonksiyonu")
        print("8. En Büyük Ortak Bölen")
        print("9. Asallık Testi")
        print("10. Daha Hızlı Fibonacci Hesabı")
        print("11. Çıkış")
        
        
        girilen_sayi = int(input("Lütfen seçenek giriniz: "))

        if girilen_sayi ==  1: # k'ninci En Kucuk Elemani Bulma
            k = int(input("Lütfen k değerini giriniz: ")) 
            tam_sayi_listesi = tam_sayi_listesi_inputu_al() 
            kninciEnKucukEleman = k_kucuk(k, tam_sayi_listesi) 
            print()
            print(f"k'ninci en küçük eleman: {kninciEnKucukEleman}") 
            print()
                            
        elif girilen_sayi ==  2: # En Yakin Cifti Bulma
            k = int(input("Lütfen en yakın çiftin bulunacağı sayıyı giriniz: ")) 
            tam_sayi_listesi = tam_sayi_listesi_inputu_al() 
            en_yakin_cift_sonuc = en_yakin_cift(k, tam_sayi_listesi) 
            print()
            print(f"En yakın çift {en_yakin_cift_sonuc[0]} ve {en_yakin_cift_sonuc[1]}") 
            print()
                
        elif girilen_sayi ==  3: # Bir Listenin Tekrar Eden Elemanlarini Bulma
            tam_sayi_listesi = tam_sayi_listesi_inputu_al() 
            tekrar_eden_elemanlar_listesi = tekrar_eden_elemanlar(tam_sayi_listesi) 
            print()
            print("Tekrar eden elemanlar: ", end="") 
            for sayi in tekrar_eden_elemanlar_listesi:
                print(f"{sayi}", end=" ")
            print()
        elif girilen_sayi ==  4: # Matris Carpimi

            
            print("A matrixi için elemanları giriniz (satır satir):")
            A_satir_sayisi = int(input("A matrixindeki satır sayisi: "))
            A_sutun_sayisi = int(input("A matrixindeki sütun sayisi: "))
            A = []

            for i in range(A_satir_sayisi):
                satir = []
                for j in range(A_sutun_sayisi):
                    eleman = int(input(f"A[{i}][{j}] elemanını giriniz: "))
                    satir.append(eleman)
                A.append(satir)

            print("B matrixi için elemanları giriniz (satır satır):")
            B_satir_sayisi = int(input("B matrixindeki satır sayısı:: "))
            B_sutun_sayisi = int(input("B matrixindeki sütun sayısı:: "))
            B = []

            for i in range(B_satir_sayisi):
                satir = []
                for j in range(B_sutun_sayisi):
                    eleman = int(input(f"B[{i}][{j}] elemanını giriniz: "))
                    satir.append(eleman)
                B.append(satir)


            matris_carpimi_sonuc = matris_carpimi(A, B) 
            print()
            print(f"Matris çarpımı sonucu: {matris_carpimi_sonuc}") 
            print()

        elif girilen_sayi ==  5: # Bir Text Dosyasindaki Kelimelerin Frekansini Bulma
            dosya_konumu = input("Lütfen text dosyasının konumunu giriniz: ") 
            kelime_frekans_sonuc = kelime_frekansi(dosya_konumu) 
            print()
            for kelime in kelime_frekans_sonuc:
                print(f"{kelime}={kelime_frekans_sonuc[kelime]}") 
            print()

        elif girilen_sayi ==  6: # Liste Icinde En Kucuk Degeri Bulma
            tam_sayi_listesi = tam_sayi_listesi_inputu_al() 
            en_kucuk_deger_sonuc = en_kucuk_deger(tam_sayi_listesi) 
            print()
            print(f"Listenin en küçük değeri: {en_kucuk_deger_sonuc}") 
            print()
        elif girilen_sayi ==  7: # Karekok Fonksiyonu
            N = int(input("Lütfen karekökü alınacak sayıyı giriniz: ")) 
            x_0 = float(input("Karekök için ilk tahmini giriniz: ")) 

            karekok_sonucu = karekok(N, x_0)
            print()
            print(f"Karekökün sonucu: {karekok_sonucu}") 
            print()

        elif girilen_sayi ==  8: # En Buyuk Ortak Bolen
            sayilar_stringi = input("Lütfen en büyük ortak böleni bulunacak sayılar arasında boşlukla giriniz: ") 
            sayilar_listesi = sayilar_stringi.split(' ') 
            sayilar = [int(sayi) for sayi in sayilar_listesi] 
            eb_ortak_bolen_sonucu = eb_ortak_bolen(sayilar[0], sayilar[1]) 
            print()
            print(f"Bu iki sayının en büyük ortak böleni: {eb_ortak_bolen_sonucu}") 
            print()
        elif girilen_sayi ==  9: # Asallik Testi
            asal_kontrol_sayisi = int(input("Lütfen asallığı kontrol edilecek sayıyı giriniz: ")) 
            print()
            if asal_veya_degil(asal_kontrol_sayisi): 
                print("Girdiğiniz sayı asal.") 
            else: 
                print("Girdiğiniz sayı asal değil.")
            print()
        elif girilen_sayi ==  10: # Daha Hizli Fibonacci Hesabi
            N = int(input("Hızlı Fibonaccisi bulunacak sayıyı giriniz: ")) 
            hizlandirici_sonuc = hizlandirici(N, 1, 1, 0) 
            print()
            print(f"Fibonacci serisinin {N}. sayısı: {hizlandirici_sonuc}") 
            print()

        elif girilen_sayi ==  11: # Çıkış
            pass 
        else:  
            print()
            print("Lütfen geçerli bir sayı giriniz.") 
            print()
            


if __name__ == "__main__":
    main() # Main fonksiyonunu çalıştır.