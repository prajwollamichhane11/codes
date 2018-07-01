#include<iostream>
using namespace std;

int main(){
  int n;
  cin >> n;
  int a[n];
  int summ = 0;

  for(int j = 0 ; j < n ; j++){
    cin >> a[j];
  }
  for (int i = 0 ; i < n ; i++){
    cout << a[i] << endl;
    summ = summ + a[i];
  }
  cout << summ;
}

