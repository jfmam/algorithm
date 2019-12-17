#include<iostream>
#include <ctime>
using namespace std;

const int N = 100000;
int arr[N + 1];
int* arr2;

void CheckTime(int a[], int n)
{
	int i = 0;
	bool Sorted = true;
	for (i = 1; i < n; i++) {
		if (a[i] > a[i + 1]) Sorted = false;
		if (!Sorted) break;
	}
	if (Sorted) cout << "정렬 완료." << endl;
	else cout << "정렬 오류 발생." << endl;
}

void merge(int left, int right)
{
	int mid = (left + right) / 2;

	int i = left;
	int j = mid + 1;
	int k = left;
	while (i <= mid && j <= right)
	{
		if (arr[i] <= arr[j])
			arr2[k++] = arr[i++];
		else
			arr2[k++] = arr[j++];
	}

	int tmp = i > mid ? j : i;

	while (k <= right) arr2[k++] = arr[tmp++];

	for (int i = left; i <= right; i++) arr[i] = arr2[i];
}//합병

void partition(int left, int right)//분할
{
	int mid;
	if (left < right)
	{
		mid = (left + right) / 2;
		partition(left, mid);
		partition(mid + 1, right);
		merge(left, right);
	}
}//left <right 가될 때까지 계속 분할한다

int main()
{
	double start_time;

	srand(time(NULL));
	arr2 = new int[N + 1];
	for (int i = 1; i <= N; i++)  arr[i] = rand();
	start_time = clock();
	partition(1, N);
	cout << "합병 정렬의 실행 시간 (N = " << N << ") : " << clock() - start_time << endl;
	CheckTime(arr, N);
}
