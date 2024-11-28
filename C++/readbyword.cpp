#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream fp;

    fp.open("text2.txt", ios::in);

    string word;

    while (fp>>word)        
    {
        if(word=="x")
        cout<<"\nfound x";
        cout<<word<<endl;
    }
    
    return 0;
}