# Problem Set 2: Singly Linked List
# Problem 2.1: Reverse Linked List.
# Given the head of a singly linked list, reverse the list, and return the reversed list.

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


    
 

    # for empty array 

    def reverse(self):
        prev = None
        curr = self.head 
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr  
            curr = temp
        self.head = prev



    def __str__(self):
        ret_str = '['
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str += ']'
        return ret_str




def reverse_array(l):
    prev = None
    curr = l.head 
    temp = l.head
    while temp is not None:
        temp = curr.next
        curr.next = prev
        prev = curr  
        curr = temp
    l.head = prev
    







# l = Linkedlist()
# l.push(1)
# l.push(2)
# l.push(3)
# l.push(4)
# l.push(5)





l = Linkedlist()
for i in range (1,6):
    l.push(i)

print("Original list:" , l)
reverse_array(l)
print("Reversed list:" , l)



l = Linkedlist()
for i in range (1,3):
    l.push(i)

print("Original list:" , l)
reverse_array(l)
print("Reversed list:" , l)



l = Linkedlist()

print("Original list:", l)   # []
l.reverse()
print("Reversed list:", l) 






