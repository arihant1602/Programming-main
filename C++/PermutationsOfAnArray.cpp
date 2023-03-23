#include<bits/stdc++.h>
using namespace std;
void printArray(int arr[], int count){
    int i;
    cout<<"[";
    for ( i = 0; i < count; i++)
    {
        cout<<arr[i];
        if( i != count-1){
            cout<<",";
        }
    }
    cout<<"]"<<endl;
}

string arraytoString(int arr[], int arrayLen){
    string s, t;
    s += "[";
    for (int i = 0; i < arrayLen; i++)
    {
        t = to_string(arr[i]);
        s += t;
        if ( i < arrayLen-1){
            s += ",";
        }
        
    }
    s += "]";
    return s;

    
}
void arrayRandomize(int arr[], int arrayLen, int newArr[]){
    srand(time(NULL));
    int i, temp;
    for ( i = 0; i < arrayLen; i++)
    {
        newArr[i] = arr[i];
    }
    
    for ( i = 0; i < arrayLen; i++)
    {
        int j = rand() % (arrayLen-1);
        temp = newArr[i];
        newArr[i] = newArr[j];
        newArr[j] = temp;
    }      
}

int factorial(int a){
    int fac = 1;
    for (int i = 1; i < a+1; i++)
    {
        fac *= i;
    }
    return fac;
}
int main(){
    int a[5] = {1,2,3,4,5}, b[5];
    for (int i = 0; i < 5; i++)
    {
        arrayRandomize(a, 5, b);
        printArray(b, 5);
    }
    
}
