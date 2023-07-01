/*
3 3
1 2 3
4 5 6
7 8 9

OUTPUT: 1 5 3

4 5
1 2 3 4 8
8 9 7 5 3
1 2 5 4 3
2 1 0 7 9

OUTPUT: 1 9 5 5 8
  */
#include<stdio.h>
int main(){
int r,c;
scanf("%d %d",&r,&c);
int mat[r][c];
for(int i = 0;i<r;i++){
  for(int j = 0;j<c;j++){
    scanf("%d",&mat[i][j]);
  }
}
int i= 0,j=0;
while(i==j && i<=c/2){
  printf("%d ",mat[i][j]);
  i++;
  j++;
}
i-=2;
while(i>=0 && j<=c){
  printf("%d ",mat[i][j]);
  i--;
  j++;
}
}
