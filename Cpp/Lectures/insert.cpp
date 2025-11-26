//---------------------------------[INSERT]-----------

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
        // Kyuki last ek pointer hai jo nodes ke beech move karega.
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
    void insert(int index, int val)
    {
        Node *new_node = new Node(val);

        if (index == 0)
        {
            cout << "Case 1" << endl;
            new_node->next = head;
            head = new_node;
            cout << "Inserted: " << to_string(val) << "at index" << to_string(index) << endl;
            return;
        }

        // for other indices:
        cout << "Case 2:";
        Node *temp = head;
        int counter = 0;
        Node *prev = nullptr;
        while (temp != nullptr && counter < index)
        {
            prev = temp;
            temp = temp->next;
            counter++;
        }
        prev->next = new_node;
        new_node->next = temp;
        cout << "Inserted: " << to_string(val) << "at index" << to_string(index) << endl;
    }
};

int main()
{
    LinkedList l;
    l.Push(1);
    l.Push(2);
    l.Push(3);
    l.Push(4);
    l.toString();
    l.insert(2, 3);
    l.insert(0, 2);