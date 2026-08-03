#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> numbers = {1, 2, 3, 4, 5};
    
  for (int i = 0; i < numbers.size(); i++) {
    cout<<numbers.size();  
    numbers.pop_back();
    numbers.push_back(i);
  }

  cout << "vector size is: " << numbers.size() << endl;
}