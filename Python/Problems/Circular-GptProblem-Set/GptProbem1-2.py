# 🧠 Question 1 (Medium):
# A circular linked list contains some nodes with integer values.
# Write a program to split the circular linked list into two halves.
# If the number of nodes is odd, the extra node should go in the first list.
# Example:
# Input: 10 -> 20 -> 30 -> 40 -> 50 -> (back to 10)
# Output:
# First Half: 10 -> 20 -> 30 -> (back to 10)
# Second Half: 40 -> 50 -> (back to 40)



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
        if self.head is None:
            return "[]"

        ret_str = ""
        temp = self.head
        while temp is not None: 
            ret_str += str(temp.val) + " -> "
            temp = temp.next
            if temp == self.head:
                break
        ret_str += "(back to " + str(self.head.val) + ")"
        return ret_str


    def split_array(self):
        last = self._get_last()

        if self.head is None or self.head.next == self.head :
            return self.head , None
        
        slow = self.head  # 1
        fast = self.head  # 1
               # 2, 3                           # 3,5
        while fast.next != self.head and fast.next.next != self.head :
            fast = fast.next.next # 3 , 5
            slow = slow.next  # 2 , 3
# 1 2 3 4 5

        head1 = self.head # 1
        head2 = slow.next  # slow-> 3 , slow.next -> 4  

        slow.next = self.head #  3.next -> 1 


        temp = head2   # 4
              # 5 , 1            # 1 
        while temp.next != self.head: 
             temp = temp.next   # temp = 1
        temp.next  = head2   # 4
                     
        return head1 , head2 




cll = Ring()
for val in [1, 2, 3, 4, 5]:
    cll.push(val)

head1, head2 = cll.split_array()

first = Ring()
first.head = head1
print("First Half:", first)

second = Ring()
second.head = head2
print("Second Half:", second)
