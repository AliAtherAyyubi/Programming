#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream fp;
    fp.open("text2.txt",ios::in);
    char ch;
    fp>>ch;
    // fp.get(ch);
    cout<<ch;

    while (fp>>ch)
    {
        cout<<endl<<ch;
    }
    

    // ofstream output("output1.txt",ios::out);
    // output<<s;

    return 0;
}