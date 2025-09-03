class Queue:
    def __init__(self):
        self.values = []
    
    def enqueue(self, ele):
        self.values.append(ele)
    
    def dequeue(self):
        if self.values:
            removed = self.values.pop()
            print("Removed element:", removed)
        else:
            print("Queue is empty. Cannot dequeue.")
    
    def dequeueat(self, ele):
        if ele in self.values:
            self.values.remove(ele)
            print(f"Removed element: {ele}")
        else:
            print(f"Element {ele} not found in queue.")
    
    def seek(self):
        if self.values:
            return self.values[-1]  # Return top of Queue
        else:
            return None
        
    def show(self):
        print("Queue:", self.values)

# Test
s = Queue()
s.enqueue(10)
s.enqueue(20)
print("Top element (seek):", s.seek())
s.show()
s.dequeueat(20)
s.dequeue()
s.show()
