#include<iostream>

using namespace std;

int main()
{
    int n1=0;
    int n2=1;
    int n3;
    int size=10;
    int arr[size];

    for (int i = 0; i < size; i++)
    {
        /* code */
        n3=n2+n1;
        arr[i]=n3;
        n1=n2;
        n2=arr[i];
    }

    cout<<"\n Fibonnaci series: ";
    for (int i = 0; i < size; i++)
    {
        /* code */
        cout<<arr[i]<<" ";
    }
    
    
    
  
}
