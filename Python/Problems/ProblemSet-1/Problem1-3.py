
# Problem 3:

# Given the head of singly linked list,
#  find middle node of the linked list.
# If the number of nodes is odd, return the middle node.
# If the number of nodes is even,
#  there are two middle nodes, so return the second middle node.
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 3 
# Explanation: There are 5 nodes in the linked list
#  and there is one middle node whose value is 3.


# Input: 10->20->30->40->50->60
# Output: 40
# Explanation: There are 6 nodes in the linked list,
#  so we have two middle nodes: 30 and 40,
#  but we will return the second middle node which is 40.


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



        
    def middle(self):
        if self.head is None:
            raise Exception("No elements in the list")

        slow = self.head
        fast = self.head 
        while fast is not None and fast.next is not None:
            slow = slow.next  # 2, 3, 4
            fast = fast.next.next  # 3, 5, None
   
        return slow.val


  

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
for i in range(1, 10): 
    l.push(i)
print(l)
print("Middle of list (odd): ",l.middle())
l.push(6)
print(l)
print("Middle (even) {Right one}:",l.middle())