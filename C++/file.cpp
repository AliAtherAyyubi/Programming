#include<iostream>
#include<fstream>

using namespace std;

int main(){

        // to write in file //
    ofstream out("text1.txt");

    string str="\nthis is ofstream class function and file...";
    out<<str;

        // to read from file //

    ifstream in("text2.txt");
    string str1;
    in>>str1;
    getline(in,str1);
    cout<<str1;
 
}