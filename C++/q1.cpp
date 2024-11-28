#include<iostream>
using namespace std;


int min_jumps(int arr[], int start,int end)
{
    if(start == end)
        return 0;

    int min = __INT_MAX__;  // Max value of int

    for(int idx = 1; arr[start] >= idx && end >= start + idx; idx++)
    {
        int jumps = min_jumps(arr, start + idx, end) + 1;
        if(min > jumps)
            min = jumps;
    }
    return min;
}

int main()
{
    int arr[] = {1, 1, 4, 1, 1, 1, 1, 2, 1, 1};
    int length= sizeof(arr)/sizeof(arr[0]);
    int ans = min_jumps(arr, 0, length);
    cout<<ans;
}