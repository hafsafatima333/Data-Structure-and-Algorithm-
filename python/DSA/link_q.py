    #==----------------------------------------------------[-PUSH-]--------------------------------------------------------

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
        

        last = self.head # 10
        while last.next is not None: # 20
            last = last.next # 20
        last.next = new_node # 30
        


    def __str__(self):
        ret_str = '['
        temp = self.head #  2 
        while temp is not None:
            ret_str += str(temp.val) + ', '  #[1,2,3]
            temp = temp.next #2 

        ret_str = ret_str.rstrip(', ')
        ret_str += ']'
        return ret_str





    def count_nodes(self):
        count = 0
        temp = self.head    
        while temp is not None:
            count += 1
            temp = temp.next

        return count
    


    def total_sum(self):
        sum = 0
        temp = self.head
        while temp is not None: #1,2,3  
            sum += temp.val
            temp = temp.next 

        return sum
    
       

    def largest_num(self):
        largest = self.head.val  # 1 2 3 4 
        temp = self.head #1,2,3,4
        while temp is not None:
            if(temp.val > largest):
                largest = temp.val #4
            
            temp = temp.next #4 

        return largest  #4
    

     

    def search_val(self,val):
        temp = self.head
        found = False
        while temp is not None:
            if (temp.val == val):
                found = True

            temp = temp.next

        return found 


    #-----------------------------------------------------[-Pop-]----------yuhuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu



    def pop(self):     # []
        #Case 1
        if self.head is None:
            raise Exception("Array is empty")
        

        #case 2 -> if we want to remove the only element ina n array   # [ 1 ] [ ]
        if self.head.next is None:
            val = self.head.val # 1
            self.head = None
            return val # => 1
        

        
        #case 3 --> if we want to remove the last element of an array

        temp = self.head # 1      # [1, 2, 3, 4]
        while temp.next is not None:
            prev = temp # 1, 2, 3
            temp = temp.next # 2, 3, 4

        val = temp.val #4
        # [1, 2, 3, 4]
        prev.next = None
        # [1, 2, 3]

        return val




#------------------------------------------INSERT----------------------------------------------------

    def insert(self, index, val):
        new_node = Node(val)      


        if (index == 0):
            print("Case # 1")
            new_node.next = self.head       
            self.head = new_node             
            return f"Inserted {val} at index {index}"

        
#for other indices: 
        print("Case # 2")
        temp = self.head               
        counter = 0
        while temp is not None and counter < index:
            prev = temp         
            temp = temp.next      
            counter += 1        
        
        prev.next = new_node 
        new_node.next = temp
        return f"Inserted {val} at index {index}"                    

#---------------------------------------------------[-REMOVE-]--------------------------------------------------------------

def remove(self, val):
    temp = self.head

#check the first node:
    if temp is not None:
        if temp.val == val:
            print("case 1:")
            self.head = temp.next
            # temp = None
            return
        

        #lets move to next nodes
        # temp holds the value of the node that will be deleted

#2nd case:

    while temp is not None:
        if temp.val == val:
            break

        prev = temp
        temp = temp.next 


   #3rd case

    if temp is None:   #not found
        print("Given elements does not found! ((Error))")
        return 
    


    #4th case
    
    print("Case 2.2:")
    prev.next = temp.next   #just lose the reference to delete node


Linkedlist.remove = remove


#main(){}

l = Linkedlist()
l.push(1)
l.push(2)
l.push(3)
l.push(4)

print(l)
print("Elements present in an array: ", l.count_nodes())
print("Sum of all elements: ", l.total_sum())
print("The largest number in an array: " ,l.largest_num())
print("Desired element present in an array: " , l.search_val(5))
print("3rd case: " , l.pop())
print("Insert:", l.insert(3, 5))
print("Insert:", l.insert(0, 6))

l.remove(2)
print(l)


l.remove(12)
print(l)


l.remove(1)
print(l)

# print(l)

      



