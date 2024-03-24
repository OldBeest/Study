#include <stdio.h>

int main(void)
{   
    int arr1[3][4];
    int arr2[7][9];

    printf("세로 3 x 가로 4 = %d\n", sizeof(arr1));
    printf("세로 7 x 가로 9 = %d\n", sizeof(arr2));
    
    return 0;
}