#include<bits/stdc++.h>
using namespace std;
 
int minTurn(int n, int k)
{
    if (n%2 == 0)
        n++;
    if (k%2 == 0)
        return min((k - 0)/2, (n - 1 - k)/2);
 
    return min((k - 1)/2, (n - k)/2);
}
 
int main(){
    int n, k;
    cin >> n;
    cin >> k;
    cout << minTurn(n,k) << endl;
    return 0;
}
