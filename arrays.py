# %% Arrays

# bir liste oluşturmak

import numpy as np
import array


def create(n):
    lst = []
    for i in range(n):
        no = int(input("Enter the number "))
        lst.append(no)
    return lst

# listeyi yazdırmak


def display(a):
    print("The data in the array are : ")
    print(a)


def access(a, i):  # access'in türkçesi erişmek demektir. a listeye eşit i ise bir indexse
    # index sıfırdan küçük olamaz aynı zamanda da listenin büyüklüğünden de fazla olamaz.

    if i >= 0 and i <= len(a)-1:
        print("Elemanın indexi ", i, "tir. eleman ise ", a[i], "dir.")

    else:
        print("Girdiğiniz değer geçerli bir index değildir.")


def insert(lst, indx, number):
    if indx < 0 or indx > len(lst):
        print("Girdiğiniz index dizi uzunluğu dışındadır.")
        return lst
    else:
        lst.insert(indx, number)
        return lst


def delete(a, i):
    if i < 0 or i >= len(a):
        print("Girdiğiniz index dizi uzunluğu dışındadır.")
        return a
    else:
        a.remove(a[i])
        return a


# burası da ana program
n = int(input("Kaç elemanlı bir dizi oluşturmak istediğinizi yazın :"))
Arr = create(n)
display(Arr)

k = int(input("Kaçıncı indexteki elemanı yazdırmak istediğinizi yazın :"))
access(Arr, k)

p = int(input("Kaçıncı indexse eleman yazdırmak istediğinizi yazın :"))
s = int(input("Şimdide " + str(p) + ". indesine eklemek istediğiniz sayıyı girin :"))
insert(Arr, p, s)
display(Arr)


b = int(input("Kaçıncı indexseteki elemanı silmek istediğinizi yazın :"))
delete(Arr, b)
display(Arr)


# %% Dictionary-Sözlük

def create():
    A = {}
    n = int(input("Kaç elemanlı bir sözlük oluşturmak istiyorsunuz: "))

    for i in range(n):
        value = int(
            input(f"{i} indeksine eklemek istediğiniz değeri yazınız: "))
        A[i] = value

    return A


def display(A):
    for i in range(len(A)):
        print(f"[{i} : {A[i]}]", end=" ")
    print()


def access(A, i):

    if i < 0 or i >= len(A):
        print("Geçersiz değer.")
    else:
        print(f"{i} anahtarındaki değer {A[i]}'dir.")


def insrt(A, i, x): 
    if i < 0:
        print("Location is below the range")
    elif i > len(A):
        print("Location is out of the range")
    else:
        # son elemandan başlayıp (len(A)-1) ilk elemana doğru gidiyor
        for j in range(len(A)-1, i-1, -1):
            A[j+1] = A[j]
        A[i] = x
        return A


def delete(A, i):
    if i < 0:
        print("Location is below the range")
    elif i > len(A):
        print("Location is out of the range")
    else:
        del A[i]
        for j in range(i, len(A)):  # son elemandan başlayıp (len(A)-1) ilk elemana doğru gidiyor
            A[j] = A[j+1]
        del A[(len(A)-1)]
        return A


A = create()
display(A)

i = int(input("Değerine bakmak istediğiniz anahtarı girin: "))
access(A, i)

k = int(input("Hangi indexe eklemek istiyorusnuz: "))
x = int(input("Ne eklemek istiyorsunuz"))
insrt(A, k, x)
display(A)
p = int(input("Hangi anahtarı silmek istiyorsunuz."))
delete(A, p)
display(A)

# %% import array


A = array.array('i', [1, 2, 3])
print(A)


# %% Numpy


A = np.array([1, 2, 3], dtype='int')
print(A)

B = np.array([1, 2, 3], 'I')
print(B)

# %% Class


class Arr:
    def __init__(self):
        self.maxSize = 10
        self.size = 0
        self.items = list()

    def readArray(self):
        number = int(
            input("\nDiziye kaç tane sayı eklemek istiyorsunuz(Sayı, 10'dan az olsun.) :"))
        if(number > self.maxSize or number <= 0):
            print("\nGirdiğiniz değer aralığın dışındadır.\n")

            return
        else:
            for i in range(number):
                data = int(
                    input(f"\nEklemek istediğiniz {i+1}. sayısı yazınız: "))
                self.items.append(data)
                self.size += 1

    def insertArray(self):
        if(self.size < self.maxSize):
            index = int(input("\nSayıyı eklemek istediğiniz indexi yazın."))
            print(self.items)

            if (index < 0 or index >= self.size):
                print("\nGirdiğiniz index bulunamadı.")
                print(self.items)

                return
            else:
                data = int(input("\nEklemek istediğiniz sayıyı girin."))
                self.items.insert(index, data)
                self.size += 1
                print(self.items)

        else:
            print("\nDizi doldu!")
            print(self.items)

    def searchingArray(self):
        data = int(input("\nAramak istediğiniz değeri girin: "))
        if data in self.items:
            index = self.items.index(data)
            print(f"Girdiğin değerin indexi {index}'tir")
        else:
            print("Aradığın değer listede yok.")

    def deleteArray(self):
        data = int(input("\nSilmek istediğin değeri gir"))
        if data in self.items:
            self.items.remove(data)
        else:
            print("Girdiğin değer bulunamadı.")
            
            
            
            
            
            
            
            
            
            
            
def main():
    arr=Arr()
    while True:
       option = menu()  # Menü fonksiyonunu çağırıyoruz

       if option == '1':
           arr.readArray()  # Liste oluşturma
       elif option == '2':
           arr.insertArray()  # Belirli bir index'e sayı ekleme
       elif option == '3':
           arr.searchingArray()  # Değer arama
       elif option == '4':
           arr.deleteArray()  # Değer silme
       elif option == '5':
           print("Programdan çıkılıyor...")
           break  # Programı sonlandır
       else:
           print("\nGeçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")

    
def menu():
    print("1. Liste oluşturun. ")
    print("2. Belirli bir indexe sayı ekleyin. ")
    print("3. Bir değeri arayın ve indexini öğrenin. ")
    print("4. Bir değeri silin.")
    opt = input("Uygulamak istediğiniz işlemi seçin.")
    return opt

if __name__ =='__main__':
    main()