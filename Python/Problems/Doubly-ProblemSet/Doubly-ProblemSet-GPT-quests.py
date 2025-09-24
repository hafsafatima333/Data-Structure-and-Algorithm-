
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



    def last_value(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        return temp

    def pairs(self, target):
        pairs = []
        if self.head is None:
            return 
        
        left = self.head # 1
        right = self.last_value() # 5
        # while left and right => left is not None and rigght is not None
        # [1, 2, 3, 4, 5] target = 5
        while left and right is not None and left != right and left.prev != right:
              s = left.val + right.val # 1 + 5 = 6, 1 + 4 = 5, 2 + 3 = 5
              if s == target: # true in 2nd iteration & 3rd iteration
                  pairs.append((left.val, right.val)) # (1,4) (2,3)
                  left = left.next # 2, 3
                  right = right.prev # 3, 2
              elif s < target:
                  left = left.next
              else: # s > target
                  right = right.prev # 4

        return pairs
    

if __name__ == "__main__":
    l = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        l.push(i)

    print("Original List:", l)
    target = 5
    print("Target =", target)
    print("Pairs with sum =", target, "are:", l.pairs(target))



    