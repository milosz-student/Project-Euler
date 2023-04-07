#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool palindrom(char* number){
    int number_length = strlen(number);
    for(int i=0;i<number_length/2;i++){
        if(number[i] != number[number_length-i-1]){
            return false;
        }
    }
    return true;
}

int main(){
    int max = 0;
    int i_j;
    char buffer[10];
    for(int i=100;i<1000;i++){
        for(int j=100;j<1000;j++){
            i_j = i*j;
            sprintf(buffer, "%d", i_j);
            if (palindrom(buffer)){
                if(max<i_j){
                    max = i_j;
                } 
            }
        }
    }
    printf("%i",max);
    return 0;
}

/*
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
*/
