#include <stdio.h>
#include <ctype.h>

int main()
{
    char c;
    c = getc(stdin);

    if(!isalpha(c)) {
        printf("invalid");
    }
    else {
        switch(c) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                printf("Vowel");
                break;
            default:
                printf("Consonant");
        }
    }

    return 0;
}