#include <bits/stdc++.h>
using namespace std;
int main(){
    int i = 0, j = 0, len, maxl = 0, summ, k, loop, checksum;

    cout<<"Enter length of array\n";
    cin>>len;

    int a[len], sublen = 0, maxmaxl = 0;


    cout<<"Enter array\n";
    for( i = 0; i < len; i++ )
    {
        cin>>a[i];
    }
    
    i = 0;
    j = 0;
    k = 0;
 

    while ( i < len )
    {
       if ( maxl + a[i] > maxl )
       {
           maxl = maxl + a[i];
           
           j++;  
           if( maxl > maxmaxl )
           {
               maxmaxl = maxl;
               sublen++;
           }
           
        }
    
       
    
      else
       {
           maxl = 0;
           k = 0;
       }
        i++;
        
    

    } 
    
    cout<<maxmaxl<<" is the largest sum";

    
    i = 0;
    j = len - 1;

    
    cout<<endl;

    checksum = 0;
    i = 0;
    loop = 0;

    for ( i = 0; i < len - sublen + 1; i++)
    {
        for ( loop = i; loop < i + sublen ; loop++)
        {
            checksum += a[loop];
        }
        if ( checksum == maxmaxl )
        {
            for ( loop = i; loop < i + sublen; loop++)
            {
                cout<<a[loop]<<" ";
            }
            cout<<" is the array"<<endl;
            break;
        }
        else
            {
                checksum = 0;
                loop = 0;
            }
        
    }
    

   

}