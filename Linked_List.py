class Node: # To create the new node
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList():  
    def __init__(self):   #inisalize the LinkedList
        self.head = None
    
    def insert_at_beg(self, data):  
        new_node = Node(data)       # Create a new node
        new_node.next = self.head   # Point new node to current head
        self.head = new_node        # Update head to new node
    
    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_beg(data)
        else:
            new_node = Node(data)       # Create a new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def get_len(self):
        cnt = 0
        current = self.head
        while current is not None:
            cnt += 1
            current = current.next
        return cnt
    
    def insert_at(self, location, data):
        if location < 0 or location > self.get_len():
            print('Invalid location')
            return
        if location == 0:
            self.insert_at_beg(data)
        else:
            current = self.head
            for i in range(location-1):
                current = current.next
            new_node = Node(data)          # Create a new node
            new_node.next = current.next   # Point new node to current head
            current.next = new_node        # Update head to new node
    
    def display(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=' ' )
                current = current.next
            print('END')
            

LL = LinkedList()
LL.insert_at_beg(10)
LL.insert_at_beg(20)
LL.insert_at_end(40)
LL.insert_at(4,60)
print(LL.get_len())
LL.display()
        

