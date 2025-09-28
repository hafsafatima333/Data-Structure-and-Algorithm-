#include <iostream>
using namespace std;

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

    Node *mergedTwoLists(Node *list1, Node *list2)
    {
        Node *dummy = new Node(0);
        Node *tail = dummy;

        while (list1 != nullptr && list2 != nullptr)
        {
            if (list1->val < list2->val)
            {
                tail->next = list1;
                list1 = list1->next;
            }
            else
            {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        if (list1 != nullptr)
        {
            tail->next = list1;
        }
        else
        {
            tail->next = list2;
        }

        Node *result = dummy->next;
        delete dummy;
        return result;
    }
};

int main()
{
    LinkedList l1;
    int arr1[] = {1, 2, 3};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);

    for (int i = 0; i < size1; i++)
    {
        l1.Push(arr1[i]);
    }

    LinkedList l2;
    int arr2[] = {1, 2, 4};
    int size2 = sizeof(arr2) / sizeof(arr2[0]);

    for (int i = 0; i < size2; i++)
    {
        l2.Push(arr2[i]);
    }

    LinkedList mergedList;

    mergedList.head = mergedList.mergedTwoLists(l1.head, l2.head);
    cout << "Merged List: " << mergedList.toString() << endl;
    return 0;
}
