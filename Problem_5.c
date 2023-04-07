/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/
#include <stdio.h>
#include <stdint.h>

int NWD(int a,int b){
    while(a!=b){
        if(a>b){
            a-=b;
        }
        else{
            b-=a;
        }
    }
    return a;
}


int NWW(int a, int b){
    return a*b/NWD(a,b); 
}

int main(){
    int output = 1;
    for(int i=1;i<=20;i++){
        if (output%i!=0)
            output = NWW(output,i);
    }
    printf("%i\n",output);
    return 0;
}