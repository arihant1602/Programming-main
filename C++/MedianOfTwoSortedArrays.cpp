#include <bits/stdc++.h>
#include "ArrayFuncs.cpp"
using namespace std;
int main(){
    int len1, len2;
    float i;
    cout << "Enter the length of array - 1\n";
    cin >> len1;
    cout << "Enter the length of array - 2\n";
    cin >> len2;
    int arr1[len1], arr2[len2], len = len1 + len2, arr[len1 + len2]; 
    cout << "Array - 1\n";
    arrayInput(arr1, len1);
    cout << "Array - 2\n";
    arrayInput(arr2, len2);
    arrayMerge(arr1, len1, arr2, len2, arr);
    sort(arr, arr + len);
    arrayOutput(arr, len);
    i = arrayMedian(arr, len);
    cout << i;
}