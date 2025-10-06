class Node:
    def __init__(self, val=None):
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
        while last.next != self.head:   # to find the last value  
            last = last.next

        last.next = new_node 
        new_node.next = self.head

    def _get_last(self):
    # CASE 1: Empty list
       if self.head is None:
          return None

    # CASE 2: Only one node
       if self.head.next == self.head:
          return self.head

    # CASE 3: More than one node
       temp = self.head
       while temp.next != self.head:
           temp = temp.next
       return temp



    def insert(self, index, val):
        new_node = Node(val)
        last = self._get_last()

        # CASE 1: Empty list
        if self.head is None:
            if index == 0:
                self.head = new_node
                new_node.next = self.head
            else:
                raise IndexError("Cannot insert at index " + str(index) + " because list is empty")
            return

        # CASE 2: Insert at head (index 0)
        if index == 0:
            new_node.next = self.head
            last.next = new_node
            self.head = new_node
            return

        # CASE 3: Insert at other indices
        temp = self.head
        counter = 0
        while temp is not None and counter < index:
         prev = temp
         temp = temp.next
         counter += 1

        prev.next = new_node
        new_node.next = temp

        if self.head is None and index > 0:
            raise Exception("Invalid index")


    def __str__(self):
        ret_str = "["
        temp = self.head
        while self.head is not None:
            ret_str += str(temp.val) + ", "
            temp = temp.next
            if temp == self.head: 
                break
        ret_str = ret_str.rstrip(", ")
        ret_str += "]"
        return ret_str
    # -----------------------------------------------------------------
    # remove :  


    def remove(self, val):
        if self.head is None: 
            raise Exception("Empty list error")
        
        last = self.get_last()
        temp = self.head
        
        if self.head == self.head.next and self.head.val == val:
            self.head = None
            return
        
        
        if self.head.val == val:
            self.head = self.head.next
            last.next = self.head
            return
        
        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
                if temp == last:  
                    last = prev
                return
            prev = temp
            temp = temp.next



# -------------------------
# TESTING YOUR INPUT
# -------------------------


r = Ring()
r.insert(0, 1)
r.insert(0, 2)
r.insert(1, 3)
r.insert(3, 5)
print(r)

r.remove(1)
