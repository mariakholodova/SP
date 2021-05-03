// Напишите программу, в которой создается числовой массив и для этого массива вычисляется сумма квадратов элементов массива.
#include <iostream>

using namespace std;



int main() {
    setlocale(LC_ALL, "Russian");
    int* array = new int[10];

    for (size_t i = 0; i < 10; i++) {
        cout << "Введите значение для " << i << " элемента:";
        cin >> array[i];
    }

    cout << "Массив значений: ";

    for (size_t i = 0; i < 10; i++) {
        cout << array[i] << " ";
    }
    cout << endl;

    int sum = 0;

    _asm {
        mov eax, 0
        mov ebx, array
        mov ecx, 10
        mov edx, 0
        m1:
        mov eax, [ebx]
            imul eax, eax
            add edx, eax
            add ebx, 4
            loop m1

            mov sum, edx
    };
 
    cout << "Сумма квадратов элементов: " << sum << endl;

    return 0;
}

