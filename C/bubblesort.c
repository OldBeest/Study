#include <stdio.h>


void bubble_sort(int *arr, int len)
{
    int temp;
    for(int j=0; j<len; j++)
        for(int i=j; i<len-1; i++)
        {
            if(*(arr+i) > *(arr+(i+1)))
            {
                temp = *(arr+i);
                *(arr+i) = *(arr+(i+1));
                *(arr+(i+1)) = temp;

            }
        //printf("%d 번째 : , arr[%d] = %d, arr[%d] = %d\n", i, i, *arr, i+1, *(arr+1));
        }
    for (int j=0; j<len; j++)
        printf("arr[%d] = %d\n", j, arr[j]);
       
}
int main(void){
    
    int arr[5] = {3, 1, 5, 2, 4};
    //printf("%d\n", sizeof(arr)); //20
    int len = (sizeof(arr)/sizeof(int)); // 20/4 = 5

    
    for (int j=0; j<len; j++)
        printf("arr[%d] = %d\n", j, *(arr+j));

    printf("\n");
    bubble_sort(arr, len);
    
    return 0;

}
