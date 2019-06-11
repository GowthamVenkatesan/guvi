// fijhiuewf
#include <stdio.h>

int main()
{
    int n;
    int a;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &a);
        if(a % 2 == 0 && i % 2 == 1)
            printf("%d ", a);
        else if(a % 2 == 1 && i % 2 == 0)
            printf("%d ", a);
    }

    return 0;
}
