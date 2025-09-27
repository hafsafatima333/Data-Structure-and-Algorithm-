
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
    }

    int middle_right_element()
    {
        if (head == nullptr)
        {
            runtime_error("List is empty");
        }
        Node *slow = head;
        Node *fast = head;
        while (fast != nullptr && fast->next != nullptr)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow->val;
    }
};

int main()
{

    // Here is a simple concept which i used in for loop:
    //     arr = {1, 2, 4, 5, 7, 8}
    // int = 4 bytes (normally)

    // sizeof(arr) = 6 * 4 = 24 bytes
    // sizeof(arr[0]) = 4 bytes

    // size = 24 / 4 = 6

    LinkedList l;
    int arr[] = {1, 3, 5, 7, 9, 2, 4, 6};
    int size = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < size; i++)
    {
        l.Push(arr[i]);
    }
    cout << l.toString() << endl;
    cout << "Middle right element: " << l.middle_right_element() << endl;

    return 0;
}