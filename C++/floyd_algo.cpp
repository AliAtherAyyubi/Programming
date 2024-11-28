#include <iostream>
#include <math.h>
using namespace std;
// Floyd's Algorithm //
#define nV 4
#define INF 999

int min(int n1, int n2)
{
    if (n1 < n2)
        return n1;

    return n2;
}
void printMatrix(int matrix[][nV])
{
    for (int i = 0; i < nV; i++)
    {
        for (int j = 0; j < nV; j++)
        {
            if (matrix[i][j] == INF)
                printf("%4s", "INF");
            else
                printf("%4d", matrix[i][j]);
        }
        cout << endl;
    }
}
void floyd_algo(int A[][nV])
{

    for (int k = 0; k < nV; k++)
        for (int i = 0; i < nV; i++)
            for (int j = 0; j < nV; j++)
                A[i][j] = min(A[i][j], A[i][k] + A[k][j]);

    cout<<"\nShortest Path Matrix:\n ";
    printMatrix(A);
}


int main()
{
    int graph[nV][nV] = {{0, 3, INF, 5}, {2, 0, INF, 4}, {INF, 1, 0, INF}, {INF, INF, 2, 0}};
    cout<<"\n Matrix of given Graph:\n";
    printMatrix(graph);
    floyd_algo(graph);
}