// #Problem Set 2 : Singly Linked List
// #Problem 2.1 : Reverse Linked List.
// #Given the head of a singly linked list, reverse the list, and return the reversed list.

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

    // #for empty array
    void reverse()
    {
        if (head == nullptr)
        {
            cout << "List is empty! Cannot reverse" << endl;
            return;
        }
        Node *prev = nullptr;
        Node *curr = head;
        while (curr != nullptr)
        {
            Node *temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        head = prev;
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

    // void reverse_array(LinkedList &l)
    // {
    //     Node *prev = nullptr;
    //     Node *curr = l.head;
    //     Node *temp = nullptr;
    //     while (curr != nullptr)
    //     {
    //         temp = curr->next;
    //         curr->next = prev;
    //         prev = curr;
    //         curr = temp;
    //     }
    //     l.head = prev;
    // }
};

int main()
{
    LinkedList l;
    for (int i = 0; i < 0; i++)
    {
        l.Push(i);
    }
    cout << "Original List: " << l.toString() << endl;
    l.reverse();
    cout << "Reversed List: " << l.toString() << endl;
}
