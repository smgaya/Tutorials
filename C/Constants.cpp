#include <stdio.h>

int main()
{
    const int  LENGTH = 10;
    const int  WIDTH = 5;
    const char NEWLINE = '\n';
    int area;

    area = LENGTH * WIDTH;
    printf("Area: %d", area);
    printf("%c", NEWLINE);

    return 0;
}

