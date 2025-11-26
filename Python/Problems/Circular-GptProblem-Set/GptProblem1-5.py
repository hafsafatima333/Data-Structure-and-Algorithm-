# Question 2 (Tricky):
# Write a program to check whether a given circular linked list is sorted or not (in ascending order).
# Example:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> (back to 1)
# Output: True
# Input: 10 -> 5 -> 20 -> 30 -> (back to 10)
# Output: False

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class Ring:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return 
        
        last = self.head
        while last.next != self.head :
            last = last.next 

        last.next = new_node
        new_node.next = self.head

    

    def _get_last(self):
        if self.head is None:
            return None
        if self.head.next ==  self.head:
            return self.head
        temp = self.head 
        while temp.next != self.head:
            temp = temp.next  
        return temp
        


    def __str__(self):
        ret_str = "["
        temp = self.head
        while self.head is not None:
            ret_str += str(temp.val) + ", "
            temp = temp.next 
            if temp == self.head:
                break
        ret_str = ret_str.rstrip(", ")
        ret_str += "]"
        return ret_str
    


    def sorted(self):
        if self.head is None or self.head.next == self.head : 
            return True 

        temp = self.head 
        while temp.next != self.head:
            if temp.val > temp.next.val:
             return False
            temp = temp.next 
           
        return True
    

r = Ring()
for i in [1,4,2,3,5]:
    r.push(i)
print(r)
r.sorted()
print("The given array is not sorted: " ,r.sorted())



r = Ring()
for i in [1,2,3,4,5]:
    r.push(i)
print(r)
r.sorted()
print("The given array is  sorted: " ,r.sorted())