import os
os.system('cls')

def bilprima(n):
    if n<2:
        return False
    else:
        for i in range (2,n):
            if n%i==0 :
                return False
        return True

def bilmegaprima(n):
    angkaprima={2,3,5,7}
    bp=[]
    tp=[]
    for digit in str(n):    
        if int(digit) in angkaprima:
            bp.append(digit)
        else:
            tp.append(digit)
    if bp and not tp:  
        print(f"{n} adalah bilangan megaprima karena {str(bp).replace('[','').replace(']','')} adalah bilangan prima")
        return True
    else:
        print(f"{n} bukan bilangan megaprima karena {str(tp).replace('[','').replace(']','')} bukan bilangan prima")
        return False
    

print("PROGRAM BILANGAN MEGAPRIMA\n")
while True:
    listprima=[]
    listmegaprima=[]
    jbmp=0
    kiri=int(input("Input Bilangan Kiri = "))
    kanan=int(input("Input Bilangan Kanan = "))
    print()
    if kiri<kanan :
        for i in range (kiri,kanan+1):
            if bilprima(i):
               listprima.append(i)
        print(f"Semua bilangan prima dari {kiri} hingga {kanan} adalah {str(listprima).replace('[','').replace(']',' ')}")
        for n in listprima:
            if bilmegaprima(n):
                listmegaprima.append(n)
                jbmp+=1
        print(f"Banyak bilangan megaprima antara bilangan {kiri} dan {kanan} adalah {jbmp} yaitu {str(listmegaprima).replace('[','').replace(']','')} ")
    else :
        print("Input bilangan bulat dimana bilangan kiri lebih kecil dari bilangan kanan!")
    print()
    ulang=input("Apakah anda ingi nmengulang program ini? (Y/T) = ").strip().upper()
    if ulang == 'T' :
        print("Terima kasih telah menggunakan program ini!")
        break

