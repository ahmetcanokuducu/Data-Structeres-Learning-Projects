"""
Ahmet Can Okuducu
Bu kod, bir kuyruk (queue) veri yapısını tanımlar.
Sözlük kullanarak kuyruk işlemlerini gerçekleştiren bir sınıf yapısı oluşturulmuştur. 
Kuyruk, FIFO (First In First Out) ilkesine göre çalışan bir veri yapısıdır. Kuyruğun en sonuna eleman eklenir ve en başından eleman çıkarılır.
Kuyruk işlemleri şunlardır:
1. Kuyruk Oluştur: Boş bir kuyruk oluşturur.
2. Kuyruğa Eleman Ekle (Enqueue): Kuyruğun sonuna bir eleman ekler.
3. Kuyruktan Eleman Çıkar (Dequeue): Kuyruğun başından bir eleman çıkarır.
4. Kuyruğu Göster: Kuyruğun içindeki elemanları gösterir.
5. Çıkış: Programdan çıkış yapar.
"""



def create():
    Q={}
    front = 0
    rear = -1
    size = int(input("Kuyruk boyutunu giriniz: "))
    print("\nBoş kuyruk oluşturuldu.")
    return Q, front, rear, size

def isEmpty(rear):
    return rear == -1

def isFull(rear, size):
    return rear == size-1

def enqueue(Q, rear, size):
    if isFull(rear, size):
        print("\nKuyruk dolu.")

    else:
        eleman = int(input("\nKurduğa eklemek istediğiniz sayıyı giriniz:"))
        rear += 1
        Q[rear] = eleman
        print("\nKuyruğa eleman eklendi.")
    return Q, rear

def dequeue(Q,front,rear):
    if isEmpty(rear):
        print("\nKuyruk boş.")
    else:
        print("\nÇıkarılan eleman: ", Q[front])
        front += 1
        if front > rear:
            front = 0
            rear = -1
    return Q, front, rear

def display(Q, rear, front):
    if isEmpty(rear):
        print("\nKuyruk boş.")
    else:
        for i in range(front, rear+1):
            if i == rear:
                print(Q[i])
            else:
                print(Q[i], "<--", end=" ")

def menu():
    print("\n1. Kuyruk Oluştur")
    print("2. Kuyruğa Eleman Ekle")
    print("3. Kuyruktan Eleman Çıkar")
    print("4. Kuyruğu Göster")
    print("5. Çıkış")
    secim = int(input("\nSeçiminizi yapınız: "))
    return secim

def main():
    while True:
        secim = menu()
        if secim == 1:
            Q, front, rear, size = create()
        elif secim == 2:
            Q, rear = enqueue(Q, rear, size)
        elif secim == 3:
            Q, front, rear = dequeue(Q, front, rear)
        elif secim == 4:
            display(Q, rear, front)
        elif secim == 5:
            break
    


if __name__ == "__main__":
    main()