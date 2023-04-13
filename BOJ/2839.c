#include <stdio.h>
int a;int b;int c;int j;int i;
void main(){
    scanf("%d",&a);
    i=a/5;
    b=a;
    for(;i>=0;i--){
        c=b-(i*5);
        if(c%3==0){
            j=c/3;
            break;
        }
    }
    j||(a%5==0)?printf("%d",i+j):printf("-1");
}