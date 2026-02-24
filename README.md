# Data Structures Learning Projects

Veri Yapıları ve Algoritmalar kapsamında yaptığım öğrenme projeleri.

## Projeler 

1) **Queue.java**
   Java kullanılarak yapılan kuyruk yapısı.

2) **Stack.java**
   Java Kullanılarak yapılan yığın yapısı.

3) **Agac.py**
    Bu kod, bir ikili arama ağacı (Binary Search Tree) sınıfını tanımlar. İkili arama ağacı, her düğümün en fazla iki alt düğümü olduğu ve sol alt düğümün değeri kök düğümün değerinden küçük, sağ alt düğümün değeri ise kök düğümün değerinden büyük olduğu bir veri yapısıdır.
   
4) **kuyruklar.py**
   Bu kod, bir kuyruk (queue) veri yapısını tanımlar. Kuyruk, FIFO (First In First Out) ilkesine göre çalışan bir veri yapısıdır. Kuyruğun en sonuna eleman eklenir ve en başından eleman çıkarılır.
   
   Kuyruk işlemleri şunlardır:
   1. Kuyruk Oluştur: Boş bir kuyruk oluşturur.
   2. Kuyruğa Eleman Ekle (Enqueue): Kuyruğun sonuna bir eleman ekler.
   3. Kuyruktan Eleman Çıkar (Dequeue): Kuyruğun başından bir eleman çıkarır.
   4. Kuyruğu Göster: Kuyruğun içindeki elemanları gösterir.
   5. Çıkış: Programdan çıkış yapar.

5) **kuyruklarSınıf.py**
   Bu kod "kuyruklar.py" kodunun class yapısı ile yapılmış halidir. 

6) **kuyruklarSözlük.py**
   Bu kod "kuyruklar.py" kodunun sözlük yapısı ile yapılmış halidir.  

7) **Yıgınlar.py**
   Bu kod, bir yığın (stack) veri yapısını tanımlar.
   Fonksiyonlar kullanılarak yığın işlemleri gerçekleştirilmiştir.
   Yığın, LIFO (Last In First Out) ilkesine göre çalışan bir veri yapısıdır. Yığının en üstüne eleman eklenir ve en üstünden eleman çıkarılır.
   Yığın işlemleri şunlardır:
   1- Push: Yığının en üstüne bir eleman ekler.
   2- Pop: Yığının en üstünden bir eleman çıkarır.
   3- Peek: Yığının en üstündeki elemanı gösterir.
   4- Display: Yığının içindeki elemanları gösterir.
   5- Çıkış: Programdan çıkış yapar.

8) **YıgınlarSınıf.py**
   Bu kod, "Yıgınlar.py" kodunun class yapısı ile yapılmış halidir.

9) **YıgınlarSözlük.py**
   Bu kod, "Yıgınlar.py" kodunun sözlük yapısı ile yapılmış halidir.

10) **Sıralama.py** 
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
    
11) **arrays.py**
    Diziler (listeler) ile ilgili temel işlemleri içeren çalışma dosyasıdır.

    İçerdiği konular (genel olarak):
    - Liste oluşturma
    - Eleman ekleme / silme
    - Eleman görüntüleme
    - İndeks ile erişim
    - Dictionary (sözlük) örnekleri
    - `array` modülü / `numpy` ile temel denemeler
    - Sınıf (`class`) yapısı ile menü tabanlı kullanım örnekleri

   

12) **baglıListe.py** (Tekli Bağlı Liste / Singly Linked List)
Bu dosyada temel bir tekli bağlı liste yapısı bulunmaktadır.

#### İçerdiği yapılar
- `Node` sınıfı
- `tekliBagliListe` sınıfı
- Menü tabanlı kullanım

#### Yapabildiği işlemler
- Liste oluşturma (kullanıcıdan veri alarak)
- Listeyi yazdırma
- Menü üzerinden işlem seçme

> Kullanıcı veri girişini `"bitti"` yazarak sonlandırabilir.

---

13) **circularLinkedList.py (Dairesel Bağlı Liste / Circular Linked List)
Bu dosyada dairesel bağlı liste yapısına yönelik daha kapsamlı bir uygulama bulunmaktadır.

#### İçerdiği yapılar
- `Node` sınıfı
- `ClinkendList` sınıfı
- Menü tabanlı kullanım

#### Temel işlemler
- Listenin elemanlarını yazdırma
- Başa ekleme
- Sona ekleme
- Belirli bir elemandan sonra ekleme
- Belirli bir elemandan önce ekleme
- İlk düğümü silme
- Son düğümü silme
- Belirli düğümü silme
- Belirli bir düğümden sonra / önce düğüm silme

> Bu dosya eğitim amaçlı geliştirildiği için bazı isimlendirme/yazım farklılıkları bulunabilir (ör. method adları / menü metinleri). Mantık olarak bağlı liste işlemlerini pratik etmek için uygundur.
