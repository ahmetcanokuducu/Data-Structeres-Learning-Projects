""" Ahmet Can Okuducu
Bu kod, bir kuyruk (queue) veri yapısını tanımlar. Kuyruk, FIFO (First In First Out) ilkesine göre çalışan bir veri yapısıdır. Kuyruğun en sonuna eleman eklenir ve en başından eleman çıkarılır.
Kuyruk işlemleri şunlardır:
1. Kuyruk Oluştur: Boş bir kuyruk oluşturur.
2. Kuyruğa Eleman Ekle (Enqueue): Kuyruğun sonuna bir eleman ekler.
3. Kuyruktan Eleman Çıkar (Dequeue): Kuyruğun başından bir eleman çıkarır.
4. Kuyruğu Göster: Kuyruğun içindeki elemanları gösterir.
5. Çıkış: Programdan çıkış yapar.
"""

def create():
    Q = []
    front = 0
    rear = -1
    print("Boş kuyruk oluşturuldu.")
    return Q, front, rear

def isEmpty(Q, rear):
    return rear == -1

def enqueue(Q, rear):
    eleman = int(input("Kuyruğa eklemek istediğiniz elemanı giriniz: "))
    Q.append(eleman)
    rear += 1
    print("Kuyruğa eleman eklendi.")
    return Q, rear

def dequeue(Q, front, rear):
    if isEmpty(Q, rear):
        print("İşlem başarısız. Kuyruk boş.")
        return Q, front, rear
    else:
        print("Çıkarılan eleman: ", Q[front])
        front += 1
        if front > rear:
            front = 0
            rear = -1
        return Q, front, rear

def display(Q, rear, front):
    if isEmpty(Q, rear):
        print("Kuyruk boş.")
    else:
        for i in range(rear, front - 1, -1):
            if i == front:
                print(Q[i])
            else:
                print(Q[i], "-->", end=" ")

def menu():
    print("1. Kuyruk Oluştur")
    print("2. Kuyruğa Eleman Ekle")
    print("3. Kuyruktan Eleman Çıkar")
    print("4. Kuyruğu Göster")
    print("5. Çıkış")

if __name__ == "__main__": 
    Q, front, rear = create()  # Kuyruğu başlangıçta oluştur
    while True:
        menu()
        secim = int(input("Seçiminizi yapınız: "))
        if secim == 1:
            Q, front, rear = create()
        elif secim == 2:
            Q, rear = enqueue(Q, rear)
        elif secim == 3:
            Q, front, rear = dequeue(Q, front, rear)
        elif secim == 4:
            display(Q, rear, front)
        elif secim == 5:
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim.")