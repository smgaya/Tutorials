#include <stdio.h>

struct status1
{
   unsigned int widthValidated;
   unsigned int heightValidated;
};

struct status2
{
   unsigned int widthValidated : 1;
   unsigned int heightValidated : 1;
};

int main()
{
   printf("Memory size occupied by status1 : %d\n", sizeof(status1));
   printf("Memory size occupied by status2 : %d\n", sizeof(status2));
   return 0;
}

