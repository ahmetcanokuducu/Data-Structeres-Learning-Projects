"""
Ahmet Can Okuducu
Bu kod, bir yığın (stack) veri yapısını tanımlar.
Class yapısı kullanılarak yığın işlemleri gerçekleştirilmiştir.
 Yığın, LIFO (Last In First Out) ilkesine göre çalışan bir veri yapısıdır. Yığının en üstüne eleman eklenir ve en üstünden eleman çıkarılır.
Yığın işlemleri şunlardır:
1- Push: Yığının en üstüne bir eleman ekler.
2- Pop: Yığının en üstünden bir eleman çıkarır.
3- Peek: Yığının en üstündeki elemanı gösterir.
4- Display: Yığının içindeki elemanları gösterir.
5- Çıkış: Programdan çıkış yapar.
"""

class Stack:
    def __init__(self,size):
        self.stack = []
        self.top = -1
        self.maxSize = size
        print("Yığın oluşturuldu. Max boyutu: ",self.maxSize)

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.maxSize - 1
    
    def push(self):
        if self.isFull():
            print("Yığın dolu. Eleman eklenemez.")
        else:
            eleman = input("Eklemek istediğiniz elemanı giriniz: ")
            self.stack.append(eleman)
            self.top += 1
            print("Eleman eklendi.")

    def pop(self):
        if self.isEmpty():
            print("Yığın boş. Eleman çıkarılamaz.")
        else:
            print("Çıkarılan eleman: ",self.stack.pop())
            self.top -= 1

    def peek(self):
        if self.isEmpty():
            print("Yığın boş.")
        else:
            print("Yığının en üstündeki eleman: ",self.stack[self.top])

    def display(self):
        if self.isEmpty():
            print("Yığın boş.")
        elif self.isFull():
            print("Yığın dolu.")
            for i in range(self.top,-1,-1):
                print(i, "-->", self.stack[i])
        else:
            for i in range(self.top,-1,-1):
                print(i, "-->", self.stack[i])

    def menu(self):
        while True:
            print("\n1- Eleman ekle")
            print("2- Eleman çıkar")
            print("3- Yığının en üstündeki elemanı göster")
            print("4- Yığını göster")
            print("5- Çıkış")
            secim = input("Seçiminizi yapınız: ")
            if secim == "1":
                self.push()
            elif secim == "2":
                self.pop()
            elif secim == "3":
                self.peek()
            elif secim == "4":
                self.display()
            elif secim == "5":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Hatalı seçim. Tekrar deneyin.")

    
    #Main

if __name__ == "__main__":
    boyut = int(input("Yığın boyutunu giriniz: "))
    yigin = Stack(boyut)
    yigin.menu()
    
    
    