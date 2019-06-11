#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int k;

    for(int i = 0; i < n; i++) {
        scanf("%d", &k);
        if(k == i)
            printf("%d ", k);
    }

    return 0;
}