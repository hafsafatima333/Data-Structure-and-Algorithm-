
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
    };

    bool hasCycle()
    {

        Node *slow = head;
        Node *fast = head;
        while (fast != nullptr && fast->next != nullptr)
        {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
            {
                return true;
            }
        }
        return false;
    }
};

// for val in [3,2,0,-4]:
int main()
{
    LinkedList l;
    int arr[] = {3, 2, 0, -4};
    int size = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < size; i++)
    {
        l.Push(arr[i]);
    }
    cout << "LinkedList: " << l.toString() << endl;
    l.head->next->next->next->next = l.head->next;
    cout << boolalpha;
    cout << "Cycle present in the LinkedList: " << l.hasCycle() << endl;

    // if cycle is not present :
    LinkedList l2;
    l2.Push(1);
    cout << "LinkedList: " << l2.toString() << endl;
    l2.head = l2.head;
    cout << boolalpha;
    cout << "Cycle present in the LinkedList: " << l2.hasCycle() << endl;
    return 0;
};
