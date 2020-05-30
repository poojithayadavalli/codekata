#include <iostream>
#include <cstdio>
using namespace std;
int main() {
     int n;
     scanf("%d",&n);
      printf("%d\n",n+n/2);
      for(int i=2;i<=n;i+=2) {
          printf("%d ",i);
     }
    // printf("\n");
     for(int i=1;i<=n;i+=2) {
         printf("%d ",i);
     }
   //  printf("\n");
     for(int i=2;i<=n;i+=2) {
         printf("%d ",i);
     }
  //   printf("\n");
     return 0;
}
 
