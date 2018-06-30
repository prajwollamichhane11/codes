#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string s;
    cin >> n;
    cin >> s;
    int k;
    cin >> k;

    k %= 26;
    for (int i = 0;i < n; i++) {
        int u = s[i];
        if (u >= 'a' && u <= 'z') {
            u += k;
            if (u > 'z') {
            u = 96 + (u % 122);
            }
        } else if(u >= 'A' && u <= 'Z') {
            u += k;
            if(u > 'Z') {
                u = 64 + (u % 90);
            }
        }
        cout << (char)u;
    }
    cout << endl;
    return 0;
}

