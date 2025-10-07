# 🔁 Question 3 (Hard):
# Write a function to count the number of times a particular value 
# appears in a circular linked list.
# Example:
# Input List: 2 -> 5 -> 2 -> 7 -> 9 -> 2 -> (back to 2)
# Value to Count: 2
# Output: 3



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


    def count(self , val ):
        temp = self.head
        counter = 0 
        while temp.next != self.head:
            if temp.val == val : 
                counter += 1 
            temp = temp.next 
        return counter 



r = Ring()
for i in [1,2,3,2,4,2,5,2,6,2,7]:
    r.push(i)
print(r)
print("Count: " , r.count(2))
