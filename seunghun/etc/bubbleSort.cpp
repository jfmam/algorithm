#include <iostream>
#include <time.h> 
#include <stdlib.h>
#include "sort.h" 
using namespace std;
const int N = 10000; 

void BubbleSort(int a[], int N) {
	int i, j; 
	for (i = N; i >= 1; i--) {  
		for (j = 1; j < i; j++)     
			if (a[j] > a[j+1]) swap(a, j, j+1); //배열의 다음숫자와 비교해서 앞에것이 더크면 바꾼다
	} 
} 

int main() {  
	int i, a[N+1];  double start_time;
	srand(time(NULL)); 
	for (i = 1; i <= N; i++) a[i] = rand();
	start_time = clock(); 
	BubbleSort(a, N);  
	cout << "버블 정렬의 실행 시간 (N = " << N << ") : " << clock() - start_time << endl;  CheckSort(a, N); 
}
