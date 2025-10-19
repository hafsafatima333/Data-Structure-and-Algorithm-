class Stack:
    def __init__(self):
        self.l = []

    def push(self, val):
        self.l.append(val)

    def pop(self):
        return self.l.pop()
    
    def peek(self):
        return self.l[-1]
    

    #--x
  

    def isEmpty(self):
        if self.s is None:
            return True
        else:
            return False
        
    def count_total(self):
        counter = 0
        for _ in self.s:
            counter += 1
        return counter

    def _str_(self):
        return str(self.s)


    def is_matching(self, expression): # 3 * 3 + (4)
        opening = "{[("
        closing = "}])" 
        mapping = dict(zip(opening, closing))
        # 'key': 'value' --- [ { ( | ) } ] '{': '}', '[': ']', '(': ')' 
        stack = [] # )
        for c in expression:
            if c not in mapping.keys() and c not in mapping.values():
                continue 
            
            if c in mapping: # (
                stack.append(mapping[c]) 
            
            elif len(stack) == 0 or c != stack.pop(): # ( )
                return False
        
        return len(stack) == 0




s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.l[1])
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.is_matching("2 + (3 * 5) * ((2 * 2) + 5)"))
print(s.is_matching("[{()]"))
# print(s.is_matching("2 + (3 * 5) * ((2 * 2) + 5"))