#include <bits/stdc++.h>
using namespace std;

int main()
{
    int arr[4][4] = {
        {2, 3, 2, 8},
        {9, 4, 54, 5},
        {1, 7, 4, 11},
        {6, 1, 9, 2}};

    int rw = 0, cl = 0;
    while (cl < 4)
    {
        int mnj = cl;
        int mnk = rw;
        int k = rw + 1;
        int j = cl;
        while (j < 4)
        {
            while (k < 4)
            {
                if (arr[k][j] < arr[mnk][mnj])
                {
                    mnj = j;
                    mnk = k;
                }
                k++;
            }
            k = 0;
            j++;
        }
        int tmp = arr[mnk][mnj];
        arr[mnk][mnj] = arr[rw][cl];
        arr[rw][cl] = tmp;

        rw++;
        if (rw == 4)
        {
            rw = 0;
            cl++;
        }
    }

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}