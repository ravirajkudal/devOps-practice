class Stack:
    def __init__(self):
        self.values = []
    
    def push(self, ele):
        self.values.append(ele)
    
    def pop(self):
        if self.values:
            removed = self.values.pop()
            print("Removed element:", removed)
        else:
            print("Stack is empty. Cannot pop.")
    
    def remove(self, ele):
        if ele in self.values:
            self.values.remove(ele)
            print(f"Removed element: {ele}")
        else:
            print(f"Element {ele} not found in stack.")
    
    def seek(self):
        if self.values:
            return self.values[-1]  # Return top of stack
        else:
            return None
        
    def show(self):
        print("Stack:", self.values)

# Test
s = Stack()
s.push(10)
s.push(20)
print("Top element (seek):", s.seek())
s.show()
s.remove(20)
s.pop()
s.show()
