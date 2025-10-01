#include <iostream>
using namespace std;

class Node
{
public:
    int val;
    Node *next;
    Node *prev;

    Node(int v)
    {
        val = v;
        next = nullptr;
        prev = nullptr;
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
    //=====--------------------------------------------------------------
    //=====--------------------------------------------------------------
    //=====--------------------------------------------------------------
    //=====--------------------------------------------------------------

    void insert(int index, int val)
    {
        Node *new_node = new Node(val);

        if (index == 0)
        {
            cout << "\nInsert at index 0:" << endl;
            new_node->next = head;
            new_node->prev = nullptr;

            if (head != nullptr)
            {
                head->prev = new_node;
            }
            head = new_node;
            cout << "Inserted " << val << " at index " << index << endl;
            return;
        }

        cout << "\nInsert at index " << index << ":" << endl;
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
        new_node->prev = prev;
        if (temp != nullptr)
        {
            new_node->next = temp;
            temp->prev = new_node;
        }

        cout << "Inserted " << val << " at index " << index << endl;
    }

    //===========================
    //============================
    //==================================================================
    void remove(int val)
    {
        if (head == nullptr)
        {
            cout << "List is empty!" << endl;
            return;
        }

        // Case 1: If the head contains the value
        if (head->val == val)
        {
            Node *temp = head;
            head = head->next;
            if (head != nullptr)
            {
                head->prev = nullptr;
            }
            delete temp;
            return;
        }

        Node *temp = head;
        Node *prev = nullptr;

        // Search for the node with matching value
        while (temp != nullptr && temp->val != val)
        {
            prev = temp;
            temp = temp->next;
        }

        // If value not found
        if (temp == nullptr)
        {
            cout << "Given element not found! ((Error))" << endl;
            return;
        }

        // Case 2: Deleting in the middle or end

        prev->next = temp->next;
        if (temp->next != nullptr)
        {
            temp->next->prev = prev;
        }

        delete temp; // Free memory
    }
};

int main()
{
    LinkedList l;
    l.Push(1);
    l.Push(2);
    l.Push(3);
    l.Push(4);

    cout << "Initial List: " << l.toString() << endl;

    l.insert(2, 3);
    cout << "After inserting 3 at index 2: " << l.toString() << endl;

    l.insert(0, 2);
    cout << "After inserting 2 at index 0: " << l.toString() << endl;

    l.remove(2);
    cout << "After removing 2: " << l.toString() << endl;

    return 0;
}
