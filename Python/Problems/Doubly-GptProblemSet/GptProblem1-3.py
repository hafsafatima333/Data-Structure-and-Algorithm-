class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
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
        new_node.prev = last



    def reverse(self):
        temp = self.head # 1
        prev_node = None

        # [1, 2, 3, 4, 5, 6]
        while temp is not None: # 1, 2, 3, 4, 5, 6
            next_node = temp.next # 2, 3 , 4, 5, 6, None
            temp.next = prev_node # None, 1, 2, 3, 4, 5
            temp.prev = next_node # 2 => [2, 1], [3, 2, 1], [4, 3, 2, 1], [5, 4, 3, 2, 1], [6, 5, 4, 3, 2, 1], [None, 6, 5, 4, 3, 2, 1] 
            prev_node = temp # 1, 2, 3, 4, 5, 6
            temp = next_node # 2, 3, 4, 5, 6, None
            
        # After reversing, the previous node will be the new head
        self.head = prev_node # 6
        return self.head



    def __str__(self):
        ret_str = "["
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ", "
            temp = temp.next
        ret_str = ret_str.rstrip(", ")
        ret_str += "]"
        return ret_str


# Example:
l = LinkedList()
l.push(5)
l.push(8)
l.push(6)
l.push(9)

print("Original:", l)
l.reverse()
print("Reversed:", l)

# l.reverse()
# print(l) # 6
