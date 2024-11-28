#include <iostream>
using namespace std;

int secretKey(int key)
{
    cout<<key;

        if (key < 17)
            secretKey(secretKey(secretKey(++key)));

    return key;
}

int main()
{
    secretKey(15) ;
    return 0;
}