#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int cnt = 0;
    int n = 0;
    int dis = 0;
    cin >> n;
    {
        if (n < 100)
        {
            cout << n;
            return 0;
        }
        cnt = 99;
        for (int i = 100; i <= n; i++)
        {
            int tmp = i;
            int j = 0;
            vector<int> v(4);
            bool ch = true;
            int pos = 0;
            while (tmp > 0)
            {
                v[j] = tmp % 10;
                tmp /= 10;
                j++;
            }
            dis = v[0] - v[1];
            for (int k = 1; k < j - 1; k++)
            {
                int a = v[k] - v[k + 1];
                if (a != dis)
                {
                    ch = false;
                }
            }
            if (ch)
            {
                cnt++;
            }
        }
    }
    cout << cnt;
    return 0;
}