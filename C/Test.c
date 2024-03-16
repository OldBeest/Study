#include <stdio.h>

void print_odd(const * arr)
{

    printf("홀수 출력 : ");
    for(int i = 0; i < 10; i++)
        if (*(arr+i) % 2 == 1)
            printf("%d ", * arr+i);
}

void print_even(const * arr)
{
    printf("짝수 출력 : ");
    for(int i = 0; i < 10; i++)
        if (*(arr+i) % 2 == 0)
            printf("%d ", *arr+i);
}
int main(void)
{   
    int arr[10];
    
    for(int i = 0; i < 10; i++)
        {
        printf("입력 :");
        scanf("%d",&arr[i]);
        }      
    //printf("%d", *arr);
    print_odd(arr);
    printf("\n");
    print_even(arr);
    
    return 0;
}