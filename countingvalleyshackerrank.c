#include <stdio.h>
#include <string.h>

int main() {
long int n;
    int d=0,c=0;
    char ch;
    scanf("%ld",&n);
    n=n+1;
    while(n)
    {
        scanf("%c",&ch);
        if(ch=='U')
        {  
            d++;
         if(d==0)
            c++;   
        }
        else if(ch=='D')
            d--;
        n--;
    }
    printf("%d",c);   
    return 0;
}
