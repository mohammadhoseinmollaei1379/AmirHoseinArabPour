#include <iostream>
using namespace std;

int main() {
    string user_input;
    string user_name;
    cout << "Plaese Enter a User Name : ";
    cin >> user_name;
    cout << endl;
    while (true) {
        cout << "C:\\" << user_name;
        cin >> user_input;
    }
    return 0;
}