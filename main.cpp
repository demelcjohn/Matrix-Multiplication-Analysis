#include <iostream>
#include <random>
#define SIZE 1000

int main()
{
    std::random_device rd;
    std::mt19937 generator(rd());
    int lowerBound = -10, upperBound = 10;
    std::uniform_int_distribution<int> distribution(lowerBound, upperBound);

    int a[SIZE][SIZE], b[SIZE][SIZE], n, randomInt;

    n = 3;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            randomInt = distribution(generator);
            a[i][j] = randomInt;
        }
    }

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            randomInt = distribution(generator);
            b[i][j] = randomInt;
        }
    }

        return 0;
}