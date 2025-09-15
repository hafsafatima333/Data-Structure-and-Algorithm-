
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

    int Sum()
    {
        int sum = 0;
        Node *temp = head;
        while (temp != nullptr)
        {
            sum += temp->val;
            temp = temp->next;
        }
        return sum;
    }

    bool search_node(int val)
    {
        Node *temp = head;
        bool found = false;
        while (temp != nullptr)
        {
            if (temp->val == val)
            {

                found = true;
                break;
            }
            temp = temp->next;
        }
        return found;
    }

    // if i want to print msg like element not found so i'll use this logic:
    bool search_val(int val)
    {
        Node *temp = head;
        while (temp != nullptr)
        {
            if (temp->val == val)
            {
                return true;
            }
            temp = temp->next;
        }
        return false;
    }

    // if i want to display the postion of element too so i will do this:
    int search_index(int val)
    {
        if (val < 1)
        {
            cout << "Error: Value should be greater or equals to 1" << endl;
            return -1;
        }
        if (val > 10)
        {
            cout << "Error: Value should be less or equals to 10" << endl;
            return -1;
        }

        Node *temp = head;
        int index = 0;
        while (temp != nullptr)
        {
            if (temp->val == val)
            {
                return index;
            }
            temp = temp->next;
            index++;
        }
        return -1; // if element doesnot exist in the list so we return -1
    }

    // if i want to find largest number in the array:

    int largest()
    {

        if (head == nullptr)
        {
            throw runtime_error("List is empty!");
        }

        int largest = head->val;
        Node *temp = head->next;
        while (temp != nullptr)
        {
            if (temp->val > largest)
            {
                largest = temp->val;
            }

            temp = temp->next;
        }
        return largest;
    }

    // if i want to find index too:

    pair<int, int> largest_num()
    {
        if (head == nullptr)
        {
            throw runtime_error("List is empty!");
        }

        int largest = head->val;
        int largestIndex = 0;

        Node *temp = head->next;
        int currentIndex = 1;

        while (temp != nullptr)
        {
            if (temp->val > largest)
            {
                largest = temp->val;
                largestIndex = currentIndex;
            }
            temp = temp->next;
            currentIndex++;
        }

        return {largest, largestIndex};
    }

    //-----------------------------------------

    int pop()
    {
        if (head == nullptr)
        {
            throw runtime_error("Array is empty");
        }

        // case 2
        if (head->next == nullptr)
        {
            int val = head->val;
            delete head;
            head = nullptr;
            return val;
        }

        // 3rd case:
        // Node *temp = head;
        // Node *prev = nullptr;
        // while (temp->next != nullptr)
        // {
        //     prev = temp;
        //     temp = temp->next;
        // }
        // int val = temp->val;
        // delete temp;
        // prev->next = nullptr;
        // return val;

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

    // ------------------remove-----------------
    void remove(int val)
    {
        Node *temp = head;
        if (temp != nullptr && temp->val == val)
        {
            cout << "Case 1:" << endl;
            head = temp->next;
            delete temp; // here memory free
            return;
        }

        //----------------Case2--------------
        Node *prev = nullptr;
        while (temp != nullptr && temp->val != val)
        {
            prev = temp;
            temp = temp->next;
        }

        //-------------------3rd case
        if (temp == nullptr)
        {
            cout << "Given elements does not found! (Error)" << endl;
        }

        //=============4th case:
        cout << "Case 2.2" << endl;
        prev->next = temp->next;
        delete temp;
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
    cout << "Total nodes: " << l.count_nodes() << endl;
    cout << "The sum of nodes is: " << l.Sum() << endl;

    //---
    int num;
    cout << "Enter number: ";
    cin >> num;

    if (l.search_val(num))
    {
        cout << "Element found!" << endl;
    }
    else
    {
        cout << "Element not found!" << endl;
    }

    //---
    cout << "Enter number: ";
    cin >> num;
    int pos = l.search_index(num);
    if (pos != -1)
    {
        cout << "Element found at index: " << pos << endl;
    }
    else
    {
        cout << "Element not found in the list!" << endl;
    }

    cout << "Largest element in an array: " << l.largest() << endl;

    //--
    auto ans = l.largest_num(); // function call
    cout << "Largest element = " << ans.first << " at index = " << ans.second << endl;

    l.insert(2, 3);
    l.insert(0, 2);

    l.remove(2);
};
