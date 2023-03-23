#include <iostream>
using namespace std;
int main(){
    int m,n,i,j,a,b;
    cout<<"Enter Length and breadth of the matrix\n";
    cin>>m>>n;
    int mtr[m][n];
    cout<<"Enter the matrix";
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            cin>>mtr[i][j];

        }
    }
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            cout<<mtr[i][j]<<" ";

        }
        cout<<"\n";
        
    }
    cout<<"----------------------\n";
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            cout<<i<<j<<" ";
            

        }
        cout<<"\n";
        
    }
    cout<<"----------------------\n";
    a=-1;
    b=-1;
    for(i=0;i<m;i++){
        if(a<m){
            a++;
        }
        if(b<n){
            b++;
        }
        cout<<mtr[a][b]<<" ";
    }
    
    return 0;
    cout<<".\n";
}