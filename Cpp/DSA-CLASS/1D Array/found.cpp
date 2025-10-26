// Does value exists in Array?
#include <iostream>
using namespace std;

int main()
{
    int val;
    cout << "Enter value to be found: ";
    cin >> val;
    bool isFound = false;
    int arr[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++)
    {
        if (arr[i] == val)
        {
            isFound = true;
            break;
        }
    }
    if (!isFound)
    {
        cout << isFound;
    }
    else
    {
        cout << isFound;
    }
}