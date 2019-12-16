#pragma once
#include <iostream>
#include <time.h>
#include <stdlib.h>
using namespace std;

const int TRUE = 1;
const int FALSE = 0;
inline void swap(int a[], int i, int j)
{
	int t = a[i]; a[i] = a[j]; a[j] = t;
}
void CheckSort(int a[], int n)
{
	int i, Sorted;
	Sorted = TRUE;
	for (i = 1; i < n; i++) {
		if (a[i] > a[i + 1]) Sorted = FALSE;
		if (!Sorted) break;
	}
	if (Sorted) cout << "���� �Ϸ�." << endl;
	else cout << "���� ���� �߻�." << endl;
}