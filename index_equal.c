#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int k;
    int found = 0;

    for(int i = 0; i < n; i++) {
        scanf("%d", &k);
        if(k == i) {
            printf("%d ", k);
            found = 1;
        }
    }

    if(!found) printf("-1");
    return 0;
}
