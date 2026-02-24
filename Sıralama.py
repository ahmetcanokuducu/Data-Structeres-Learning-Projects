"""
Ahmet Can Okuducu
Bu kod, bir sıralama algoritması olan Bubble Sort, Insertion Sort, Selection Sort
ve arama algoritması olan Binary Search ve Linear Search'i tanımlar.
Sıralama algoritmaları, bir dizi veya liste içindeki elemanları belirli bir düzene göre sıralamak için kullanılır. Arama algoritmaları ise bir dizi veya liste içinde belirli bir değeri bulmak için kullanılır.
Sıralama algoritmaları:
1. Bubble Sort: Komşu elemanları karşılaştırarak ve gerektiğinde yer değiştirerek sıralama yapar.
2. Insertion Sort: Her elemanı sıralanmış kısmın doğru konumuna
yerleştirerek sıralama yapar.
3. Selection Sort: Sıralanmamış kısmın en küçük elemanını bulup sıralanmış kısmın sonuna ekleyerek sıralama yapar.
Arama algoritmaları:
1. Binary Search: Sıralı bir dizide hedef değeri bulmak için kullanılır. Diziyi sürekli olarak ikiye bölerek arama yapar.
2. Linear Search: Dizinin her elemanını sırayla kontrol ederek hedef değeri bulmaya çalışır.
"""


def bubble_sort(arr):
    # Dizinin uzunluğunu alıyoruz
    n = len(arr)
    
    # Tüm elemanları sırayla kontrol etmek için dış döngü
    for i in range(n):
        # İç döngü, her seferinde bir elemanı yerine koymak için
        for j in range(0, n-i-1):
            # Eğer soldaki eleman sağdakinden büyükse, yer değiştir
            if arr[j] > arr[j+1]:
                # Elemanları yer değiştiriyoruz
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # Sıralanmış diziyi döndürüyoruz
    return arr

# Örnek kullanım
dizi = [64, 34, 25, 12, 22, 11, 90]
print("Sıralanmamış dizi:", dizi)
sıralı_dizi = bubble_sort(dizi)
print("Sıralanmış dizi:", sıralı_dizi)



def insertion_sort(arr):
    # Dizinin uzunluğunu alıyoruz
    n = len(arr)
    
    # Dizinin her elemanını sırayla kontrol etmek için dış döngü
    for i in range(1, n):
        # Şu anki elemanı alıyoruz
        key = arr[i]
        
        # Şu anki elemandan bir önceki elemanı alıyoruz
        j = i - 1
        
        # İç döngü, şu anki elemanı doğru konuma yerleştirmek için
        while j >= 0 and key < arr[j]:
            # Eğer şu anki eleman, bir önceki elemandan küçükse, bir önceki elemanı bir sonraki konuma taşı
            arr[j + 1] = arr[j]
            # Bir önceki elemanı kontrol etmek için j'yi bir azalt
            j -= 1
        
        # Şu anki elemanı doğru konuma yerleştir
        arr[j + 1] = key
    
    # Sıralanmış diziyi döndürüyoruz
    return arr

# Örnek kullanım
dizi = [64, 34, 25, 12, 22, 11, 90]
print("Sıralanmamış dizi:", dizi)
sıralı_dizi = insertion_sort(dizi)
print("Sıralanmış dizi:", sıralı_dizi)



def binary_search(arr, target):
    # Binary search için dizinin sıralı olması gerekir
    # Önce diziyi sıralıyoruz (eğer sıralı değilse)
    arr = sorted(arr)
    
    # Sol ve sağ sınırları belirliyoruz
    left = 0  # Dizinin başlangıç indeksi
    right = len(arr) - 1  # Dizinin son indeksi
    
    # Sol sınır sağ sınırı geçmediği sürece devam et
    while left <= right:
        # Orta noktayı hesapla
        # (left + right) // 2 yerine bu formülü kullanmak integer overflow'u önler
        mid = left + (right - left) // 2
        
        # Orta nokta tam aradığımız değerse
        if arr[mid] == target:
            return mid  # Hedef değerin indeksini döndür
        
        # Eğer hedef değer orta noktadaki değerden küçükse
        # Aramanın sol yarısına odaklan
        elif arr[mid] > target:
            right = mid - 1
        
        # Eğer hedef değer orta noktadaki değerden büyükse
        # Aramanın sağ yarısına odaklan
        else:
            left = mid + 1
    
    # Eğer döngüden çıktıysak ve değeri bulamadıysak
    return -1  # Değer dizide yok

# Örnek kullanım
dizi = [11, 12, 22, 25, 34, 64, 90]
hedef = 25
print("Aranan değer:", hedef)
sonuc = binary_search(dizi, hedef)
if sonuc != -1:
    print(f"Değer dizinin {sonuc}. indeksinde bulundu")
else:
    print("Değer dizide bulunamadı")



    def selection_sort(arr):
        # Dizinin uzunluğunu alıyoruz
        n = len(arr)
        
        # Dış döngü, sıralanmamış kısmın başlangıç indeksini kontrol eder
        for i in range(n):
            # En küçük elemanın indeksini tutuyoruz
            min_idx = i
            
            # İç döngü, sıralanmamış kısımda en küçük elemanı bulmak için
            for j in range(i+1, n):
                # Eğer daha küçük bir eleman bulunursa
                if arr[j] < arr[min_idx]:
                    # Yeni minimum indeksi güncelle
                    min_idx = j
                    
            # En küçük elemanı, sıralanmamış kısmın başına taşı
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Sıralanmış diziyi döndürüyoruz
        return arr

    # Örnek kullanım
    dizi = [64, 34, 25, 12, 22, 11, 90]
    print("Sıralanmamış dizi:", dizi)
    sıralı_dizi = selection_sort(dizi)
    print("Sıralanmış dizi:", sıralı_dizi)



#lineer arama

def linear_search(arr, target):
    # Dizinin her elemanını sırayla kontrol et
    for i in range(len(arr)):
        # Eğer hedef değer bulunursa
        if arr[i] == target:
            return i  # Hedef değerin indeksini döndür
    
    # Eğer hedef değer dizide yoksa
    return -1  # Değer dizide yok   



# Örnek kullanım
dizi = [11, 12, 22, 25, 34, 64, 90]
hedef = 25
print("Aranan değer:", hedef)
sonuc = linear_search(dizi, hedef)
if sonuc != -1:
    print(f"Değer dizinin {sonuc}. indeksinde bulundu")
else:
    print("Değer dizide bulunamadı")

        