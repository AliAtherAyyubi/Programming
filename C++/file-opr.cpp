#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    // file handling operation in c++ //

    // to create file or write in file //

    /* 
    fstream fio("text3.txt", ios::out);
    string s="Hello I am a Text no 3";
    if(!fio){
        cout<<"file can't create";
    }
    else{
        cout<<"file created successfully";
        fio<<s;
        fio.close();
    }
    */

    // read file //

    string str;

    fstream fio2("text3.txt", ios::in);

    // fio2>>str;

    while(getline(fio2,str)){
        cout<<"\n"<<str;
    }
   


    return 0;
}

