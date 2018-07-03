#include <stdio.h>
static int count = 1;
int a =0;
int b = 1;
int fib = 1;

int fibonacci(int n) {
    b = fib;
    fib = a + b;
    a = b;
    
    count++;
    while(count <= n){
        return (fibonacci(n));
    }
    return b;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", fibonacci(n));
    return 0;
}
