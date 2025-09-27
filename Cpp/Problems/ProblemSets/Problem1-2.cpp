
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

    int count_nodes()
    {
        int count = 0;
        Node *temp = head;
        while (temp != nullptr)
        {
            count++;
            temp = temp->next;
        }
        return count;
    }

    int same_elements(int val)
    {
        int count = 0;
        Node *temp = head;
        while (temp != nullptr)
        {
            if (temp->val == val)
            {
                count++;
            }
            temp = temp->next;
        }
        return count;
    }
};

int main()
{
    LinkedList l;
    int arr[] = {2, 3, 4, 5, 2, 8, 7, 7, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < size; i++)
    {
        l.Push(arr[i]);
    }
    cout << l.toString() << endl;
    cout << "Occurrences of 5: " << l.same_elements(5) << endl;

    return 0;
}