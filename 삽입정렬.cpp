#include <iostream>
#include <time.h> 
#include <stdlib.h> 
#include "sort.h" 
using namespace std;
const int N = 10000;
void InsertionSort(int a[], int N) {
	int i, j, v;  
	for (i = 2; i <= N; i++) {
		v = a[i]; j = i;  
		while (a[j-1] > v) {  
			a[j] = a[j-1]; j--;   
		}    
		a[j] = v;  
	}
} 
int main() { 
	int i, a[N+1]; 
	double start_time; 
	a[0] = -1; // 감시 키  
	srand(time(NULL)); 
	for (i = 1; i <= N; i++)
		a[i] = rand();
start_time = clock();  
InsertionSort(a, N); 
cout << "삽입 정렬의 실행 시간 (N = " << N << ") : " << clock() - start_time << endl;  CheckSort(a, N);
}
