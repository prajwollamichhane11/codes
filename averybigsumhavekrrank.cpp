#include<iostream>
using namespace std;

int main(){
    long long n1, summ = 0;
        
    
    int n;
    cin >> n;
    
    int a[n];
    
    for(int i = 0 ; i < n ; i++){
        cin >> n1;
        summ = summ + n1;
    }
    cout << summ;
}
