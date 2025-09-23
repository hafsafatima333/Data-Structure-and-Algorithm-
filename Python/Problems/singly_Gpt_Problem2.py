class Node: 
    def __init__(self, val=None):
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


    def middle_average(self):
        slow = self.head
        fast = self.head
        prev = None   # slow ke ek step pehle ka pointer

        # slow 1 step, fast 2 steps
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # agar fast None hai → list even thi
        if fast is None:
            return (prev.val + slow.val) / 2
        else:
            # odd case → ek hi middle
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


# main code
l = Linkedlist()

l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
l.push(6)

print("Original Linked List:", l)
print("Middle / Average of Linked List:", l.middle_average())
