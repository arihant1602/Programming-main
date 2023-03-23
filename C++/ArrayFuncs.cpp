#include <bits/stdc++.h>
using namespace std;
void arrayInput(int arr[], int arrLen){
    cout<<"Enter the array\n";
    for (int i = 0; i < arrLen; i++)
    {
        cin>>arr[i];
    }
}
void arrayOutput(int arr[], int arrLen){
    for (int i = 0; i < arrLen; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
void arrayMerge(int arr1[], int len1, int arr2[], int len2, int newArr[]){
    for (int i = 0; i < ( len1 + len2 ); i++)  
    {
        if (i < len1)
        {
            newArr[i] = arr1[i];
        }
        else{
            newArr[i] = arr2[i - len1];
        }
    }
}
float arrayMedian(int arr[], int len){
    if (len % 2 == 1)
    {
        return arr[(len/2)];
    }
    else
    {
        float i = (arr[len/2]+ (arr[len/2 - 1]))/2;
        return i;
    }
}
