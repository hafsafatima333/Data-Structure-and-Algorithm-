// Insertion
#include <iostream>
using namespace std;

int main()
{
    int size = 5;
    int arr[6] = {1, 2, 3, 4, 5};
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    int index;
    cout << "Enter index: ";
    cin >> index;
    int value;
    cout << "Enter value: ";
    cin >> value;
    for (int i = size; i > index; i--)
    {
        arr[i] = arr[i - 1];
        // arr[5] = arr[4] => 1,2,3,4, ,5
        // arr[4] = arr[3] => 1,2,3, ,4,5
        // arr[3] = arr[2] => 1,2, ,3,4,5
    }
    arr[index] = value;
    // 1,2,9,3,4,5
    size++;
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
}

// // Insertion
// #include <iostream>
// using namespace std;

// int main(){
//     cout << ""}