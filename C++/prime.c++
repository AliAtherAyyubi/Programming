#include<iostream>
using namespace std;

int main()
{
    int i, n,flag=0;

    // cout<<"\n Enter any number : ";
    // cin>>n;
    n=2;
    if(n==0 || n==1){
        flag=1;
    }

    for ( i = 2; i <= n/2; ++i)
    {
        /* code */
        if( n % i==0){
            flag=1;
            break;
        }
    }

    if(flag==0)
    cout<<"\n Prime Number";
    else
    cout<<"\n Not a prime number";
    

    return 0;
}