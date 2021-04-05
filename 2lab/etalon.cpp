#include <iostream>

int main()
{
    int array[10] = {
        0b10000000,
        0b00001000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b10001000
    };
    int cnt = 0;
    for (size_t i = 0; i < 10; i++)
    {
        if (!(array[i] & 0b10001000)) {
            cnt++;
        }
    }

    std::cout << cnt << std::endl;
}
