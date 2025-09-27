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
    

    
    def count(self):
        counter = 0
        temp = self.head 
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter
    
#[1,2,2,3,2,1]  =>2 
    
    def same_elements(self, val ):
        counter = 0
        temp = self.head
        while temp is not None:
            if temp.val == val:
                counter += 1  # 1, 2, 3
            temp = temp.next
        return counter
    




    
l = LinkedList()

for i in [1, 2, 2, 2, 3, 4]:
    l.push(i)

print(l)
print(l.count())

print(l)
print(l.same_elements(2))