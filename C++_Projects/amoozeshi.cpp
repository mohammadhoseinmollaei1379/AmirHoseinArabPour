#include <iostream>

int main() {
    const int Count = 10;
    for (int number = 1; number <= Count; ++number) {
        for (int num = 1; num <= number; ++num) {
            std::cout << number * num << ' ';
        }
        std::cout << '\n';
    }
    return 0;
}