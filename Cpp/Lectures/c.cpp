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

    void push(int val)
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

    int pop()
    {
        if (head == nullptr)
        {
            throw runtime_error("Array empty");
        }
        // case2

        if (head->next == nullptr)
        {
            int val = head->val;
            delete head;
            head = nullptr;
            return val;
        }
        // case3

        Node *temp = head;
        Node *prev = nullptr;
        while (temp->next != nullptr)
        {
            prev = temp;
            temp = temp->next;
        }
        int val = temp->val;
        delete temp;
        prev->next = nullptr;
        return val;
    }

    //---------------------------------[INSERT]-----------

    void insert(int index, int val)
    {

        Node *new_node = new Node(val);
        if (index == 0)
        {
            cout << " Case 1<< endl";
            new_node->next = head;
            head = new_node;
            cout << "Inserted at " << to_string(val) << "at index" << to_string(index) << endl;
        }

        cout << "Case 2" << endl;
        Node *temp = head;
        Node *prev = nullptr;
        int counter = 0;
        while (temp != nullptr && counter < index)
        {
            prev = temp;       // 2
            temp = temp->next; // 3
            counter++;
        }
        prev->next = new_node; // 5
        new_node->next = temp; // 3
        cout << "Inserted: " << to_string(val) << "at index" << to_string(index) << endl;

    } // 1 2 5 3

    // def remove(self, val):
    //     temp = self.head

    // #check the first node:
    //     if temp is not None:
    //         if temp.val == val:
    //             print("case 1:")
    //             self.head = temp.next
    //             # temp = None
    //             return

    //         #lets move to next nodes
    //         # temp holds the value of the node that will be deleted

    // #2nd case:

    //     while temp is not None:
    //         if temp.val == val:
    //             break

    //         prev = temp
    //         temp = temp.next

    //    #3rd case

    //     if temp is None:   #not found
    //         print("Given elements does not found! ((Error))")
    //         return

    //     #4th case

    //     print("Case 2.2:")
    //     prev.next = temp.next   #just lose the reference to delete node

    void remove(int val)
    {
        Node *temp = head;
        Node *prev = nullptr;
        if (temp != nullptr)
        {
            if (temp->val == val)
            {
                cout << "1st case of remove: " << endl;
                head = temp->next;
                delete head;
            }
        }
    }
};

int main()
{
    LinkedList l;
    l.push(1);
    l.push(2);
    l.push(3);
    l.push(4);
    cout << l.toString() << endl;

    l.insert(2, 3);
    l.insert(0, 2);
};