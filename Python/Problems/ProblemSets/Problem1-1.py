

# Problem 1:
# Given a singly linked list, the task is to remove every kth node of the linked list.
#  Assume that k is always less than or equal to the length of the Linked List.
# Examples : 
# Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
# Output: 1 -> 3 -> 5
#  Explanation: After removing every 2nd node of the linked list,
#  the resultant linked list will be: 1 -> 3 -> 5 .
# Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
# Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
# Explanation: After removing every 3rd node of the linked list, the resultant 
# linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.
# Hint: The idea is to traverse the linked list while maintaining a counter to track node positions. 
# Every time the counter reaches k, update the next pointer of the previous node to skip the current kth node, 
# effectively removing it from the list. Continue this process until reaching the end of the list.
#  This method ensures that the kth nodes are removed as required while preserving the rest of the list structure.


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





    def removekthNode(self, key):
         if key <= 0 or self.head is None:
             return 
         # key = 2
         count = 1 # 2 , 3 , 4  , 5
         prev = None
         temp = self.head # 1, 2 , 3 , 4  , 5

         while temp is not None:
             # count =  1 , 2
             if count % key == 0:   # 1 % 2 = 1   , 2 % 2 = 0  , 3 % 2 = 1  , 4 % 2 = 0 , 5 % 2 = 1
                 if prev is None:
                     self.head = temp.next 
                     temp = temp.next 
                 else:
                     prev.next  = temp.next # 3 ,5
                     temp = temp.next  # 2  , 3 ,5

             else: 
                 prev = temp  # 1, 3 , 5
                 temp = temp.next # 2 , 4 , none

             count += 1  # 2 , 3  , 4 , 5 , 6
                 
# 1 , 3 , 5




        




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
for i in range (1,10):
    l.push(i)

print ("Original array: " , l)
l.removekthNode(2)
print("New Array: " , l)


