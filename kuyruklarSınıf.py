"""
Ahmet Can Okuducu
Bu kod, bir kuyruk (queue) veri yapısını tanımlar. Kuyruk, FIFO (First In First Out) ilkesine göre çalışan bir veri yapısıdır. Kuyruğun en sonuna eleman eklenir ve en başından eleman çıkarılır.
Kuyruk işlemleri şunlardır:
1. Kuyruk Oluştur: Boş bir kuyruk oluşturur.
2. Kuyruğa Eleman Ekle (Enqueue): Kuyruğun sonuna bir eleman ekler.
3. Kuyruktan Eleman Çıkar (Dequeue): Kuyruğun başından bir eleman çıkarır.
4. Kuyruğu Göster: Kuyruğun içindeki elemanları gösterir.
5. Çıkış: Programdan çıkış yapar.
"""
class Kuyruk:
    def __init__(self):
        self.Q = []
        self.front = 0
        self.rear = -1
        self.size = int(input("Kuyruğunuzun boyutunu giriniz: "))
        print("\nBoş kuyruk oluşturuldu.")

    def isEmpty(self):
        return self.rear == -1
    
    def isFull(self):
        return self.rear == self.size - 1
    
    def enqueue(self):
        if self.isFull():
            print("\nKuyruk dolu.")
        else:
            eleman = int(input("\nKuyruğa eklemek istediğiniz elemanı giriniz: "))
            self.rear += 1
            self.Q.insert(self.rear, eleman)
            print("\nKuyruğa eleman eklendi.")

    def dequeue(self):
        if self.isEmpty():
            print("\nKuyruk Boş.")

        else:
            print("\nÇıkarılan eleman: ", self.Q[self.front])
            self.front += 1
            if self.front > self.rear:
                self.front = 0
                self.rear = -1
    
    def display(self):
        if self.isEmpty():
            print("\nKuyruk boş.")
        else:
            for i in range(self.front, self.rear + 1):
                if i == self.rear:
                    print(self.Q[i])
                else:
                    print(self.Q[i], "<--", end=" ")

    
       
    

if __name__ == "__main__":
    
    while True:
        print("\n1. Kuyruk Oluştur")
        print("2. Kuyruğa Eleman Ekle")
        print("3. Kuyruktan Eleman Çıkar")
        print("4. Kuyruğu Göster")
        print("5. Çıkış")
        secim = int(input("\nSeçiminizi yapınız: "))
        if secim == 1:
            kuyruk = Kuyruk()
        elif secim == 2:
            kuyruk.enqueue()
        elif secim == 3:
            kuyruk.dequeue()
        elif secim == 4:
            kuyruk.display()
        elif secim == 5:
            break
        else:
            print("\nGeçersiz seçim.")