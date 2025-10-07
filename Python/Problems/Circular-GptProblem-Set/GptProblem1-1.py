
# Write a complete Python program to implement a Circular Linked List that supports 
# insertion at a specific index and deletion by value.
# You are required to:
# Create a class Node and Ring.
# Implement the following functions inside Ring:
# insert(index, val) → inserts a node at the given index.
# remove(val) → deletes the first node containing the given value.
# __str__() → returns the circular list in readable format (e.g., [10, 20, 30]).
# Then, perform the given operations step-by-step and show the final output.
# r = Ring()
# r.insert(0, 10)
# r.insert(1, 20)
# r.insert(1, 15)
# r.insert(3, 25)
# r.insert(0, 5)
# print("After Insertions:", r)

# r.remove(15)
# r.remove(5)
# r.remove(25)
# print("After Removals:", r)
# Expected Output Format:
# less
# Copy code
# After Insertions: [5, 10, 15, 20, 25]
# After Removals: [10, 20]

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class Ring:
    def __init__(self):
        self.head = None

    # def push(self, val):
    #     new_node = Node(val)
    #     if self.head is None:
    #         self.head = new_node
    #         new_node.next = self.head
    #         return 
        
    #     last = self.head
    #     while last.next != self.head :
    #         last = last.next 

    #     last.next = new_node
    #     new_node.next = self.head

    

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



     
    def insert(self, index , val):
        new_node = Node(val)

        # case 1 
        if self.head is None:
            if index == 0 :
               self.head =  new_node 
               new_node.next = self.head
            else:
                raise IndexError("Can't insert at your desired index" + str(index) + "because list is empty")
            return 
        # case 2
        last = self._get_last()
        if index == 0:
            new_node.next = self.head
            last.next = new_node
            self.head = new_node
            return 
        
        # case 3 
        temp = self.head
        counter = 0 
        while temp is not None and counter < index :
            prev = temp 
            temp = temp.next 
            counter += 1
        prev.next = new_node
        new_node.next = temp 

        if self.head is None and index > 0 : 
            raise Exception("Invalid Index")

r = Ring()
r.insert(0, 10)
r.insert(1, 20)
r.insert(1, 15)
r.insert(3, 25)
r.insert(0, 5)
print("After Insertions:", r)

