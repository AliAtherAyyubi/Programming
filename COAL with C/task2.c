#include <stdio.h>

// void loop(){
//     int n=0;
//     for (int i = 0; i < 5; i++)
//     {
//         n++;
//     }
//     printf("n= %d",n);
// }

// int factorial(){
//     int n=7;
//     int r=1;
//     while (n>0)
//     {
//         r *=n;
//         n=n-1;
//     }
//     return r;

// }

// void example_for(){
//     int n=7;
//     int r=1;
//     // int temp=2;
//     for (int i = 0; i <= n; i++)
//     {
//         /* code */
//          r +=n;
//          if(r<2){
//             r=4;
//          }
//     }

// }

// void main(){
//     int result= factorial();
//     printf("fact= %d", result);
// }

// void example_Switch(int n)
// {
//     int r = 1;
//     //
//     switch (n)
//     {
//     case 1:
//         r = r + 1;
//         break;
//     case 2:
//         r = 2;
//         break;
//     case 3:
//         r = 3;
//         break;
//     default:
//         break;
//     }
// }

void example2_switch(int x, int n, int *dest)
{
    int val = x;
    switch (n)
    {
    case 100:
        val *= 13;
        break;
    case 102:
        val += 10;
    /* Fall through */
    case 103:
        val += 11;
        break;
    case 104:
    case 106:
        val *= val;
        break;
    default:
        val = 0;
    }
    *dest = val;
}

int max_switch(int a, int b, int c, int n)
{

    int max;
    if (a > b && a >= c)
        max = a;
    else if (b >= a && b >= c)
        max = b;
    else
        max = c;
    switch (n)
    {
    case 0:
    case 1:
        max = max + 1;
        break;
    case 2:
        max = max + 2;
        break;
    case 3:
        max = max + 3;
        break;
    default:
        max = max + max;
    }

    return max;
}