#include <iostream>

#define SIZE 1000

void display(int a[SIZE][SIZE], int b[SIZE][SIZE], int n);

int main()
{
    return 0;
}

void display(int a[SIZE][SIZE], int n)
{
    std::cout << std::endl;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            std::cout << a[i][j] << " ";
        }
        std::cout << std::endl;
    }
}
