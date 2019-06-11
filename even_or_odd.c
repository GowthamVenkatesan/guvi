#include <stdio.h>
#include <math.h>

int main() {
    double n;
    if(scanf("%lf", &n) <= 0)    {
        printf("Invalid");
        return 0;
    }

    if(floor(n) != n) {
        printf("Invalid");
        return 0;
    }
    int nAsInt = n;
    if((nAsInt & 1) == 1)    printf("Odd");
    else                printf("Even");
    
    return 0;
}