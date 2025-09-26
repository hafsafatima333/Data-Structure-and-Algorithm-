

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, val):
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return 
        
        last = self.head
        while last.next is not None:
            last = last.next 
        last.next = new_node




    def __str__(self):
        ret_str = '['
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str += ']'
        return ret_str
    


def hasCycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False




#for 1st case:

l = LinkedList()
for val in [3,2,0,-4]:
    l.push(val)

l.head.next.next.next.next = l.head.next  #-4 points to 2
print("Cycle present in the linked list, where the tail connects to the 1st node (0-indexed): " , hasCycle(l.head))




# for second case: 

l = LinkedList()
for val in [1,2]:
    l.push(val)

l.head.next = l.head
print("Cycle present  in the linked list, where the tail connects to the 0th node: " , hasCycle(l.head))





#for third case: 
l = LinkedList()
for val in [1]:
    l.push(val)

l.head = l.head
print("There is no cycle in the linked list: " , hasCycle(l.head))












# Unprofessional but easy to understand way 


# # linked list banate hain
# n1 = ListNode(3)
# n2 = ListNode(2)
# n3 = ListNode(0)
# n4 = ListNode(-4)

# for i in [3,2,0,-4]:
#     print (i)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n2  # cycle

# # ab function call
# print("Cycle Present in the linked list: " , hasCycle(n1))  # head = n1
