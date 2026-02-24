#%% Singel Linked List

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class tekliBagliListe:
    def __init__(self):
        self.head = None
  
    
   
    def olustur(self):
        
        while True:
            
            data = input("\nEklemek istediğiniz değeri girin. Eğer başka eklemek istemiyorsanız 'bitti' yazın.")
            if data.lower()=="bitti":
                break
            try:
                data = int(data)
            except ValueError:
                print("\nLütfen geçerli bir değer girin.")
                continue
        
            yeniDugum = Node(data)
            
            if self.head == None:
                self.head = yeniDugum
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = yeniDugum
                
    def yazdir(self): 
        temp = self.head
        
        if temp == None:
            print("\nListe boş.")
            return
        while temp:
            print(temp.data, "->", end="")
            temp = temp.next
            
            
            
            
            
            
    def menu(self):
        
        while True:
            print("Tekli listeyi oluşturmak için 1'e basın")
            print("Listeyi yazdırmak için 2'ye basın.")
            opt=input("\nGerçekleştirmek istediğiniz işlemin değerini girin. İşlemleri bitirmek istiyorsanız, işlemler dışındaki herhangi bir sayıya basın: ")
            
            if opt == '1':
                self.olustur()
            elif opt == '2':
                self.yazdir()
            else:
                print("\nişlem sonlandırıldı.")
                break
                
              
             
        
lst = tekliBagliListe()
lst.menu()           
        
            
    
    
    
    
    
    