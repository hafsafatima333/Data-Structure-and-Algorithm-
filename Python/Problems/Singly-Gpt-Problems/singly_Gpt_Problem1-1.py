# Problem:
# Write a function removeGreaterThan(x) that removes all nodes from a singly linked list
# whose values are strictly greater than the given integer x.
# The function should update the head of the list if the first node(s) need to be removed.




class Node: 
    def __init__(self, val = None):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return 
        
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node





    def removeGreaterThan(self, x):
        if self.head is None:
            return 
        temp = self.head 
        prev = None
        while temp is not None:
            if temp.val > x :
                if prev is None:
                  self.head = temp.next 
                  temp = temp.next 
                else :
                  prev.next = temp.next
                  temp = temp.next
            else:
                prev = temp 
                temp = temp.next 


    def __str__(self):
        ret_str = '['
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str += ']'
        return ret_str



l = Linkedlist()
# for i in range (1,8):
l.push(1)
l.push(2)
l.push(8)
l.push(3)
l.push(9)
l.push(12)
l.push(10)



print("Original Linked List:", l)
l.removeGreaterThan(5)
print("Linked List after removing values greater than 5:", l)