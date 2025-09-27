
// # Problem 1:
// # Given a singly linked list, the task is to remove every kth node of the linked list.
// #  Assume that k is always less than or equal to the length of the Linked List.
// # Examples :
// # Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
// # Output: 1 -> 3 -> 5
// #  Explanation: After removing every 2nd node of the linked list,
// #  the resultant linked list will be: 1 -> 3 -> 5 .
// # Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
// # Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
// # Explanation: After removing every 3rd node of the linked list, the resultant
// # linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.
// # Hint: The idea is to traverse the linked list while maintaining a counter to track node positions.
// # Every time the counter reaches k, update the next pointer of the previous node to skip the current kth node,
// # effectively removing it from the list. Continue this process until reaching the end of the list.
// #  This method ensures that the kth nodes are removed as required while preserving the rest of the list structure.

#include <iostream>
using namespace std;
// int main()

class Node
{
public:
    int val;
    Node *next;

    Node(int v)
    {
        val = v;
        next = nullptr;
    }
};

class LinkedList
{
public:
    Node *head;
    LinkedList()
    {
        head = nullptr;
    }

    void Push(int val)
    {
        Node *new_node = new Node(val);
        if (head == nullptr)
        {
            head = new_node;
            return;
        }

        Node *last = head;
        while (last->next != nullptr)
        {
            last = last->next;
        }

        last->next = new_node;
    }

    // Node *prev = nullptr;

    void removeKthNode(int key)
    {
        if (key <= 0 or head == nullptr)
        {
            return;
        }

        int count = 1;
        Node *prev = nullptr;
        Node *temp = head;

        while (temp != nullptr)
        {
            if (count % key == 0)
            {
                if (prev == nullptr)
                {
                    head = temp->next;
                    temp = head;
                }
                else
                {
                    prev->next = temp->next;
                    temp = temp->next;
                }
                prev = temp;
                temp = temp->next;
            }
            count++;
        }
    }

    string toString()
    {
        string ret_str = "[";
        Node *temp = head;
        while (temp != nullptr)
        {
            ret_str += to_string(temp->val) + ", ";
            temp = temp->next;
        }

        if (ret_str.size() > 1)
        {
            ret_str.pop_back();
            ret_str.pop_back();
        }

        ret_str += "]";
        return ret_str;
    }
};

int main()
{
    LinkedList l;
    for (int i = 0; i < 10; i++)
    {
        l.Push(i);
    }
    l.removeKthNode(2);
    cout << l.toString();
    return 0;
}