#       RECURSION

# print numbers 1 till 10


# def numbers_till_10(n):
#     if(n == 11):
#         return
#     print(n)
#     numbers_till_10(n+1)

# # numbers_till_10(1)

# # print from 5 to 0
# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)

# # show(5)


# # factorial 4! = 4*3*2*1

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# # print(factorial(4))
# def sum(n):
#     if n == 0:
#         return n
#     return n + sum(n-1)

# # print(sum(10))







# array = ["Apple", "Mango", "Banana", "Grapes"]
# # indx = 0
# def print_array(array,indx):
#     if indx == len(array):
#         return
#     print(array[indx])  
#     indx += 1 
#     print_array(array,indx)  

# print_array(array,0)





# def fibonacci(n):
#     if n <= 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# # print(fibonacci(5))

# def fib(n, a = 0, b = 1):
#     if n == 0:
#         return a
#     return fib(n-1, b, a+b)

# print(fib(8))





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



    def get_first(self):
        if self.head:
          return self.head.val  
        else: 
          return None

    def last(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp.val




    #  Recursive Print
    def print_list(self, node):
        if node is None:
            return
        

        if node.val == self.get_first():  # First element
            print("[", node.val, ", ", end=" ")
        elif node.val == self.last():  # Last element
            print(node.val, "]")
       
        else:
            print(node.val, ", ", end=" ")

        self.print_list(node.next)





#------------Reverse 

    def reverse_print(self, node):
        # empty list
        if self.head is None:
            print("[]")
            return

        if node.next is None:
            print(f"[ {node.val}", end="")
        else:
            self.reverse_print(node.next)
            print(f" , {node.val}", end="")

        if node == self.head:
            print(" ]")


    def sum_nodes(self, node):
        if node is None:
           return 0
        return node.val + self.sum_nodes(node.next)


    def count_nodes(self, node):
        if node is None:
           return 0
        return 1 + self.count_nodes(node.next)



l = Linkedlist()

for i in [1, 2, 3, 4]:
    l.push(i)

print("Orginal List: " , end= " " )
l.print_list(l.head)
print("Reversed List: " , end = " " )
l.reverse_print(l.head)


print("Sum =", l.sum_nodes(l.head))
print("Count =", l.count_nodes(l.head))




     