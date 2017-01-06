#include <stdio.h>

int main()
{
    FILE *fp;
    char buff[255];

    fp = fopen("C:/Software_Development/Tutorials/C/test.txt", "r");
    fscanf(fp, "%s", buff);
    printf("1: %s\n", buff );

    fscanf(fp, "%s", buff);
    printf("2: %s\n", buff );

    fscanf(fp, "%s", buff);
    printf("3: %s\n", buff );
    fclose(fp);
}

