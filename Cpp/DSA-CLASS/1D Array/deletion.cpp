// // Deletion
// #include <iostream>
// using namespace std;

// int main()
// {
//     int size = 5;
//     int arr[5] = {2, 4, 6, 8, 10};
//     // {2,4,8,10}
//     for (int i = 0; i < size; i++)
//     {
//         cout << arr[i] << " ";
//     }
//     cout << endl;
//     cout << "Enter index: ";
//     int index;
//     cin >> index;
//     cout << "Index asked: " << index;
//     cout << endl;
//     for (int i = index; i < size; i++)
//     {
//         arr[i] = arr[i + 1];
//         // arr[2] = arr[3]_
//         // arr[3] = arr[4]
//     }
//     // cout << endl;
//     size--;
//     for (int i = 0; i < size; i++)
//     {
//         cout << arr[i] << " ";
//     }
// }

// deletion by index:
#include <iostream>
using namespace std;
int main()
{
    cout << "Deletion Process in 1D Array" << endl;
    int size = 10;
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    int index;

    cout << "Enter index you want to delete: " << endl;
    cin >> index;
    cout << endl;

    for (int i = index; i < size; i++)
    {
        arr[i] = arr[i + 1];
    }
    size--;
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
}

// deletion by value
#include <iostream>
using namespace std;

int main()
{
    // Deletion using value not index?
    int arr[5] = {1, 2, 3, 4, 5};
    int size = 5;
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    int val;
    cout << "Enter value for deletion: ";
    cin >> val;
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == val)
        { // 2nd index = 3
            for (int j = i; j < size; j++)
            {                        // 2, 3, 4
                arr[j] = arr[j + 1]; // arr[2] = arr[3] => 1,2,4, ,5 / arr[3] = arr[4] =>  1,2,4,5,  / arr[4] = arr[5] => 1,2,4,5
            }
        }
    }
    size--;
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
}