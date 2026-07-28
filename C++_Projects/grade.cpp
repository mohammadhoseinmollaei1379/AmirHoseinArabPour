#include <iostream>
using namespace std;

int main() {
    int grade ;

    cout << " Enter Value : " ;
    cin >> grade;

    switch (grade) {
    case 1 :
        cout << " Saturday " << endl;
        break;
    case 2 :
        cout << " Sunday " << endl;
        break;
    case 3 :
        cout << " Monday " << endl;
        break;
    case 4 :
        cout << " Tuesday " << endl;
        break;
    case 5 :
        cout << " Wednesday " << endl;
        break;
    case 6 :
        cout << " Thursday " << endl;
        break;
    case 7 :
        cout << " Friday " << endl;
        break;
    default:
        cout << " Wrong Entry Data!" << endl;
    }
}