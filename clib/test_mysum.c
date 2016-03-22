#include "mysum.h"
#include <stdio.h>

int main(int args, char* argv[]) {
   int a;
   int b;
   a = 1;
   b = 2;
   printf("%d+%d=%d\n", a, b, mysum(a,b));   
   return 0;
}

