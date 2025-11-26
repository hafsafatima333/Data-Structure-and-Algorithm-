# 🔄 Question 4 (Challenge):
# Given two circular linked lists, write a function to merge them into one circular linked list.
# Example:
# List 1: 1 -> 2 -> 3 -> (back to 1)
# List 2: 4 -> 5 -> 6 -> (back to 4)
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> (back to 1)
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

    def merge(self, other):
        if self.head is None:
            return other
        if other.head is None:
            return self
        
        last1 = self._get_last()
        last2 = other._get_last()

        last1.next = other.head
        last2.next = self.head
        return self




list1 = Ring()
for i in [1,2,3]:
    list1.push(i)


list2 = Ring()
for i in [4,5,6]:
    list2.push(i)
    

merged = list1.merge(list2)
print("Merged List: " , merged)








