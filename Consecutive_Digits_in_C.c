//To print the digits that are repeated in a given number in reverse order - focuses on repetition
#include<stdio.h>
int main(){
int n,c=0;
scanf("%d",&n);
while(n!=0){
  if(n%10 == (n/10)%10){
    printf("%d",n%10);
    c++;
    while(n%10==(n/10)%10){
      n/=10;
      }
  else{
    n/=10;
    }
    }
if(c == 0){
  printf("No digits are repeated");
  }
return 0;
}
