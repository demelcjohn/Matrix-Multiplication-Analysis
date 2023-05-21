#include <iostream>
#include <random>
// #include "display.h"

const int SIZE = 1000;

int main()
{
    std::random_device rd;
    std::mt19937 generator(rd());
    int lowerBound = -10, upperBound = 10;
    std::uniform_int_distribution<int> distribution(lowerBound, upperBound);

    std::cout << "Hello\n";

    int a[SIZE][SIZE], b[SIZE][SIZE], n, randomInt;

    // n = 3;
    // for (int i = 0; i < n; ++i)
    // {
    //     for (int j = 0; j < n; ++j)
    //     {
    //         randomInt = distribution(generator);
    //         a[i][j] = randomInt;
    //     }
    // }

    // for (int i = 0; i < n; ++i)
    // {
    //     for (int j = 0; j < n; ++j)
    //     {
    //         randomInt = distribution(generator);
    //         b[i][j] = randomInt;
    //     }
    // }
    // // display(a, n);
    // // display(b, n);
    return 0;
}