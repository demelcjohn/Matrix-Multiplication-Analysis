#include <iostream>
#include <random>

int main()
{
    std::random_device rd;
    std::mt19937 generator(rd());

    int lowerBound = 1;
    int upperBound = 100;

    std::uniform_int_distribution<int> distribution(lowerBound, upperBound);

    randomInt = distribution(generator);

    return 0;
}