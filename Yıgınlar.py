"""Ahmet Can Okuducu
Bu kod, bir yığın (stack) veri yapısını tanımlar.
Fonksiyonlar kullanılarak yığın işlemleri gerçekleştirilmiştir.
Yığın, LIFO (Last In First Out) ilkesine göre çalışan bir veri yapısıdır. Yığının en üstüne eleman eklenir ve en üstünden eleman çıkarılır.
Yığın işlemleri şunlardır:
1- Push: Yığının en üstüne bir eleman ekler.
2- Pop: Yığının en üstünden bir eleman çıkarır.
3- Peek: Yığının en üstündeki elemanı gösterir.
4- Display: Yığının içindeki elemanları gösterir.
5- Çıkış: Programdan çıkış yapar.
"""

def create(capacity):
    S = []
    top = -1
    print("Yığın oluşturuldu")
    return S, top, capacity

def isEmpty(top):
    return top == -1

def isFull(top, capacity):
    return top == capacity - 1

def push(S, top, capacity):
    if isFull(top, capacity):
        print("Yığın dolu")
    else:
        eklenecekSayı = int(input("Eklemek istediğiniz sayıyı giriniz: "))
        top += 1
        S.insert(top, eklenecekSayı)
        print("Yığına eklendi")
    return S, top

def pop(S, top):
    if isEmpty(top):
        print("Yığın boş")
    else:
        çıkarılanEleman = S[top]
        print("Çıkarılan eleman: ", çıkarılanEleman)
        S.remove(çıkarılanEleman)  # Elemanı listeden tamamen kaldırır
        top -= 1
    return S, top

def peek(S, top):
    if isEmpty(top):
        print("Yığın boş")
        return None
    else:
        print("Yığının en üstündeki eleman: ", S[top])
        return S[top]

def display(S, top):
    print("Top is at index: ", top)
    if isEmpty(top):
        print("Yığın boş")
    else:
        print("Yığın elemanları: ", S[:top+1])  # Yığın elemanlarını liste olarak yazdırır

def menu():
    capacity = int(input("Yığının kapasitesini giriniz: "))
    S, top, capacity = create(capacity)
    while True:
        print("\n--- Menü ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Çıkış")
        choice = int(input("Seçiminizi yapın: "))

        if choice == 1:
            S, top = push(S, top, capacity)
        elif choice == 2:
            S, top = pop(S, top)
        elif choice == 3:
            peek(S, top)
        elif choice == 4:
            display(S, top)
        elif choice == 5:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    menu()
