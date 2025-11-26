class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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
        
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node



    def __str__(self):
        ret_str = '['
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str += ']'
        return ret_str
    


def mergeTwoLists(list1, list2): #[1,2,4] , [1,3,4]
    dummy = ListNode()       # Start point    (0)
    tail = dummy             # Pointer to build merged list

    # dono lists ke nodes compare karo
    while list1 and list2:
        if list1.val < list2.val: #[1]  , [1]
            tail.next = list1   
            list1 = list1.next   
        else:
            tail.next = list2  # 1 
            list2 = list2.next   # 2
        tail = tail.next

    # jo bacha, usko attach karo
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    # return dummy.next  # merged head


    merged_list = Linkedlist()
    merged_list.head = dummy.next
    return merged_list



print("for array elements:")
l1 = Linkedlist()
for val in [1,2,4]:
    l1.push(val)


l2 = Linkedlist()
for val in [1,3,4]:
    l2.push(val)


merged_list = mergeTwoLists(l1.head,l2.head)
print(merged_list)


print("for empty list: ")

ll1 = Linkedlist()
for val in []:
    ll1.push(val)


ll2 = Linkedlist()
for val in []:
    ll2.push(val)

merged_list = mergeTwoLists(ll1.head , ll2.head)
print (merged_list)









# l1 = Linkedlist()
# for val in [1,2,4]:
#     l1.push(val)


# l2 = Linkedlist()
# for val in [1,3,4]:
#     l2.push(val)



# merged_head = mergeTwoLists(l1.head , l2.head) 

# temp = merged_head
# elements = []
# while temp:
#     elements.append(str(temp.val))
#     temp = temp.next

# print("Merged List:", "[" + ", ".join(elements) + "]")



