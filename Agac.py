"""
Ahmet Can Okuducu 

Bu kod, bir ikili arama ağacı (Binary Search Tree) sınıfını tanımlar. İkili arama ağacı, her düğümün en fazla iki alt düğümü olduğu ve sol alt düğümün değeri kök düğümün değerinden küçük, sağ alt düğümün değeri ise kök düğümün değerinden büyük olduğu bir veri yapısıdır.
"""


class Node:
    def __init__(self, key):
        # Düğümün değeri
        self.val = key
        # Sol alt düğüm
        self.left = None
        # Sağ alt düğüm
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # Ağacın kök düğümü başlangıçta None
        self.root = None

    def insert(self, key):
        # Yeni bir düğüm eklemek için yardımcı fonksiyon
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        # Eğer yeni düğümün değeri kök düğümün değerinden küçükse
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        # Eğer yeni düğümün değeri kök düğümün değerinden büyükse
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def inorder(self):
        # Inorder traversal (Sıralı Gezinti) başlatmak için yardımcı fonksiyon
        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            # Sol alt ağacı gez
            self._inorder(root.left)
            # Kök düğümü yazdır
            print(root.val, end=' ')
            # Sağ alt ağacı gez
            self._inorder(root.right)

    def search(self, key):
        # Belirli bir değeri aramak için yardımcı fonksiyon
        return self._search(self.root, key)

    def _search(self, root, key):
        # Eğer kök düğüm None ise veya kök düğümün değeri aranan değerse
        if root is None or root.val == key:
            return root
        # Eğer aranan değer kök düğümün değerinden küçükse
        if key < root.val:
            return self._search(root.left, key)
        # Eğer aranan değer kök düğümün değerinden büyükse
        return self._search(root.right, key)

# Binary Search Tree (İkili Arama Ağacı) oluştur
bst = BinarySearchTree()

# Ağaca düğümler ekle
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Inorder traversal (Sıralı Gezinti) ile ağacı yazdır
print("Inorder traversal of the given tree")
bst.inorder()

# Belirli bir değeri ara
key = 40
if bst.search(key):
    print(f"\n{key} değeri ağaçta bulundu.")
else:
    print(f"\n{key} değeri ağaçta bulunamadı.")