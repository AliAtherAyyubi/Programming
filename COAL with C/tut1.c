#include<stdio.h>


// int simple(int *xp, int y){
//     int t= *xp +y;
//     *xp=t;
//     return t;
// }

int condition(int a ,int b){
    int result=0;
l1:
    a++;
    if(a<b)
    goto l1;
    else
     result= b-a;

    return result;
}

int my_func(int x,int y){
    int s= x+y;
    s= ((s*5)-(x*7));
    int s1= s & 0xff000000;
    int s2= s1*s;
    return s2;
}

void main(){
   int res= condition(7,6);
   printf("Result: %d",res);
}