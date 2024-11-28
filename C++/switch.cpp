#include<iostream>
using namespace std;

int main()
{
    bool bag1,bag2;

    const int count=100;

    switch (count)
    {
    case (count<10) /* constant-expression */:
        /* code */
        bag1=true;
        break;
    case (count<1000):
        /* code */
        bag2=true;
        break;
    
    default:
        cout<<"error";
        break;
    }

    cout<<bag1<<endl;
    cout<<bag2<<endl;
    return 0;
}