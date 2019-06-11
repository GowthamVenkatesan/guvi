#include <stdio.h>
#include <ctype.h>

int main()
{
    char c;
    c = getc(stdin);

    printf((isalpha(c) ? "Alphabet" : "No"));
    return 0;
}