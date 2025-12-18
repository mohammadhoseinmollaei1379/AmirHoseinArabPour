#include <iostream>
using namespace std;

int main() {
    float radius, area, periphery;

    float pi = 3.14;

    cout << " Plaese Enter a Radius :" << '\a';
    cin >> radius;
    periphery = ( radius * 2 ) * pi;
    area = ( radius * radius ) * pi;
    cout << " Periphery : " << periphery << "\n"
         << " Area : " << area << endl;
    return 0;
}