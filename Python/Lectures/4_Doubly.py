class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None   #change


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        
    #case 2
        last = self.head
        while last.next is not None:
            last = last.next


        last.next = new_node
        new_node.prev = last    #change 

    def __str__(self):
        ret_str = "["
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ", "
            temp = temp.next
        ret_str = ret_str.rstrip(", ")
        ret_str += "]"
        return ret_str

    def pop(self):
        if self.head is None:
            return
        if self.head.next is None:   # agar sirf ek element ho
            self.head = None
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None

    def remove(self, val):
        if self.head.val == val:  # [1]
            self.head = self.head.next  # [] -> singly # [1,2,3]
            if self.head is not None:  # change
                self.head.prev = None
            return

        temp = self.head
        while temp is not None:
            if temp.val == val:
                break
            prev = temp  # 1, 2
            temp = temp.next  # 2, 3

        prev.next = temp.next
        if temp.next is not None:  # change # 4
            temp.next.prev = prev

    def count(self):
        counter = 0
        temp = self.head
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter



    def insert(self, index, val):
        new_node = Node(val)  # 5
        # case 1
        # [new_node => None]
        if index == 0:
            new_node.next = self.head  # [new_node,1,2,3,4]
            if self.head is not None:
                self.head.prev = None
            self.head = new_node
            return

        # case 2
        # [1, 2, 3, 4]
        temp = self.head  # 1
        counter = 0
        while temp is not None and counter < index:
            prev = temp  # 1, 2, 3
            temp = temp.next  # 2, 3, None
            counter += 1  # 1, 2, 3

        prev.next = new_node  # 5 # 1,2,3,5
        new_node.prev = prev
        # [1, 2, 3, 5]
        new_node.next = temp  # 1,2,3,5,None

        if temp is not None:
            temp.prev = new_node


    def new_push(self, val):
        # 1. insert, 2. count, 3.val
        self.insert(self.count(), val)

        

    def same_elements(self, val):
        counter = 0
        temp = self.head
        while temp is not None:
            if temp.val == val:
                counter += 1  # 1, 2, 3
            temp = temp.next
        return counter
    



# Testing
l = LinkedList()
l.push(1)
l.push(2)
l.push(2)
l.push(2)
l.push(3)
l.push(4)

print(l)
print(l.count())
l.new_push(5)
print(l)
print(l.same_elements(2))
