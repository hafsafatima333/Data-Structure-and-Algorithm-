# class Node:


#     def __init__(self, val=None):
#         self.val = val #None
#         self.username = None



#     def __str__(self):
#         input = "Hafsa"
#         self.username = input
#         return f"Hello!, {self.username}"
    

# n = Node()
# print(n)



#--------------------------


# class Node:
#     def __init__(self, val=None):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None



#     def push(self, val):
#        new_node = Node(val)

#     #no node currently 


#        if self.head is None:
#             self.head = new_node
#             return 
    

#     #otherwise, reach the end and then insert 
 
#        last = self.head 
#        while last.next is not None:
#             last = last.next

    
#        last.next = new_node 


# # LinkedList.push = push 

# #we can add functions to classes even after 


#     def __str__ (self):
#         ret_str = '['
#         temp = self.head 
#         while temp is not None:
#             ret_str += str(temp.val) + ' , '
#             temp = temp.next 


#         ret_str = ret_str.rstrip(', ')
#         ret_str += ']'
#         return ret_str


# # LinkedList.__str__ = __str__

# l = LinkedList()
# l.push(1)
# l.push(2)
# l.push(3)
# print(l)

# #print("Pop: " , l.pop())
# #print(l)




class Node:
    def __init__(self, val = None):
        self.val = val
        self.next  = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return 
        
        last = self.head 
        while last.next is not None:
            last = last.next
        last.next = new_node


    
    def __str__(self):
        ret_str = "["
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp = temp.next 

        ret_str = ret_str.rstrip(', ')
        ret_str += "]"
        return ret_str
    


    def count_node(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next

        return count
    
    
    def sum(self):
        sum = 0
        temp = self.head
        while temp is not None:
            sum += temp.val
            temp = temp.next
        return sum


    
    
    def largest_num(self):
        largest = self.head.val
        temp = self.head #1,2,3,4
        while temp is not None:
            if(temp.val > largest):
                largest = temp.val #4
            
            temp = temp.next 

        return largest  #4
    


    def largest(self):
        largest = self.head.val
        temp = self.head
        while temp is not None:
            if(temp.val > largest):
                largest = temp.val 
            temp = temp.next
        return largest 
    



    def pop(self):
        temp = self.head
        while temp.next is not None:
           prev = temp
           temp = temp.next
        val = temp.val
        prev.next = None
        print("Popped:", val)       # print bhi

        return val



l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
print("-----------Push-------------")
print(l)
print("The total number present in an array is: " , l.count_node())
print("The total sum of an array is: " , l.sum())
print("-------------Pop------------")
print("Elements before pop" , l)
l.pop()
print("Elements After pop" , l)

