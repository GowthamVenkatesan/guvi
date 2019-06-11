#include <stdio.h>

int main()
{
    int y;
    scanf("%d", &y);

    if(y < 0)   printf("invalid");
    else if(y % 400 == 0)   printf("yes");
    else if(y % 100 == 0)   printf("no");
    else if(y % 4 == 0)     printf("yes");
    else                    printf("no");
    
    return 0;
}