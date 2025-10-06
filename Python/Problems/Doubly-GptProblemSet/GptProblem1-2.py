
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

    def __str__(self):
        ret_str = "["
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ", "
            temp = temp.next
        ret_str = ret_str.rstrip(", ")
        ret_str += "]"
        return ret_str





    def split_at_position(self, idx):
        if self.head is None or idx <= 0:
            return self.head, None

        temp = self.head
        counter = 0

        while temp is not None and counter < idx:
            temp = temp.next #2 , 3 , 4
            counter += 1 #1 , 2 ,3 

        if temp is None:
            return self.head, None

        second_head = temp  # 4

        if temp.prev is not None:
            temp.prev.next = None  # 3.next-> None
            temp.prev = None  # 4->prev = None

        first_head = self.head  

        return first_head, second_head



dll = LinkedList()
for i in [1,2,3,4,5,6]:
    dll.push(i)
print("Original list: " )
print(dll)
print("Split Array: ")

head1, head2 = dll.split_at_position(3)
dll1 = LinkedList()
dll1.head = head1
dll2 = LinkedList()
dll2.head = head2
print(dll1)   # Ye __str__ wala method use karega
print(dll2)
