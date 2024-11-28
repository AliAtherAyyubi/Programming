#include <iostream>
#include <cstdlib>
#include<cmath>
#include <ctime>
using namespace std;


int check_prime(int n)
{
    if (n <=1)
        {
            return 0;
        }
    else{
        for (int i = 2; i <= sqrt(n) ; i++)
    {
        /* code */
        if (n % i == 0)
        {
            return 0;
        }
        
    }
    }
    return 1;
}

void print_array(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        /* code */
        cout << " " << arr[i];
    }
}

int main(int argc, char *argv[])
{
    // MPI_Init(&argc, &argv);

    // int nproc, rank;
    // MPI_Comm_size(MPI_COMM_WORLD, &nproc);
    // MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    const int size = 20;
    int arr[size];

    srand(time(nullptr));
    cout << "Random Array: ";
    for (int i = 0; i < size; i++)
    {
        /* code */
        arr[i] = rand() % 15;
        cout << " " << arr[i];
    }

    int prime_nmbr;

    cout << "\nPrime Numbers: ";

    for (int i = 0; i < size; i++)
    {
        /* code */
        prime_nmbr = check_prime(arr[i]);
        if (prime_nmbr == 1)
            cout << " " << arr[i];
    }
}
