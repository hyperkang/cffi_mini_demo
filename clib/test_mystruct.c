#include "mystruct.h"
#include <stdio.h>

int main(int args, char* argv[]) {
   struct MyStruct st1 = {1, 1.0};

   printf("st1.a=%d\n", st1.a);   
   ChangeStruct(&st1, 10);
   printf("st1.a=%d\n", st1.a);   

   return 0;
}


