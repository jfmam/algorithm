#include <iostream>
#include <time.h>
#include <stdlib.h>

const int N = 100000;
int a[N + 1];

using namespace std;

const int TRUE = 1;
const int FALSE = 0;

inline void swap(int a[], int i, int j)
{
	int t = a[i]; a[i] = a[j]; a[j] = t;
}
void printList(int a[], int n)
{
	int i;
	for (i = 1; i < n; i++)
		cout << a[i] << ", ";
	cout << a[i] << endl;
}
void CheckTime(int a[], int n)
{
	int i, Sorted;
	Sorted = TRUE;
	for (i = 1; i < n; i++) {
		if (a[i] > a[i + 1]) Sorted = FALSE;
		if (!Sorted) break;
	}
	if (Sorted) cout << "정렬 완료." << endl;
	else cout << "정렬 오류 발생." << endl;
}

void heapify(int a[], int h, int m)
{
	int j, v;
	v = a[h];
	for (j = 2 * h; j <= m; j *= 2) {
		if (j < m && a[j] < a[j + 1]) j++;
		if (v >= a[j]) break;
		else a[j / 2] = a[j];
	}
	a[j / 2] = v;
}

void HeapSort(int a[], int n) {
	int i;
	for (i = n / 2; i >= 1; i--)
		heapify(a, i, n);

	for (i = n - 1; i >= 1; i--) {
		swap(a, 1, i + 1);
		heapify(a, 1, i);

	}
}

void main()
{
	int i;
	double start_time;

	srand(time(NULL));
	for (i = 1; i <= N; i++) a[i] = i;

	start_time = clock();
	HeapSort(a, N);
	cout << "히프 정렬의 실행 시간 (N = " << N << ") : " <<
		clock() - start_time << endl;
	CheckTime(a, N);
}

