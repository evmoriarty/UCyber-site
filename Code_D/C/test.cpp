#include <iostream>

using namespace std;

int main(){
  double base = 5, exp = 0.5, sum = 1;
  int i = 0;

  while(i < exp){
    sum*=base;
    i++;
  }

  cout << sum << endl;

  return 0;
}
