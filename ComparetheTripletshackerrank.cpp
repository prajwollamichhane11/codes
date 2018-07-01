#include<iostream>
using namespace std;

int main(){
  int a = 0 , b = 0 ;

  int A[3],B[3];

  cin >> A[0] >> A[1] >> A[2] ;
  cin >> B[0] >> B[1] >> B[2] ;

  if(A[0] > B[0]) a++;
  else if (A[0] < B[0]) b++;

  if(A[1] > B[1]) a++;
  else if (A[1] < B[1]) b++;

  if(A[2] > B[2]) a++;
  else if (A[2] < B[2]) b++;

  cout << a <<" " << b ;
}
