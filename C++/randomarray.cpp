 #include<bits/stdc++.h>
 using namespace std;
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
int main()
{
    int arr[5] = {1,2,3,4,5};
    int newArr[5];
    arrayRandomize(arr, 5, newArr);
    for (int idx = 0; idx < 5; idx++) {
        cout << newArr[idx] << std::endl;
    }
}