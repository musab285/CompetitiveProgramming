#include <bits/stdc++.h>
#include <string>
#include <cstring>
using namespace std;

#define ll long long int
#define str string
#define forn(a, b) for (int i = a; i < b; i++)
#define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bara INT_MAX
#define chota INT_MIN
#define bohotbara LLONG_MAX
#define bohotchota LLONG_MIN
#define all(x) x.begin(), x.end()

bool isSortedasc(vector<int> &arr)
{
    for (int i = 0; i < arr.size() - 1; i++)
    {
        if (arr[i] > arr[i + 1])
            return false;
    }
    return true;
}

void solve()
{
    ll t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> p(n);
        int j = 1;
        forn(0, n)
        {
            cin >> p[i];
            if ((3 * (j + 1)) - p[i] > 0)
                cout << (3 * j) - p[i] << " ";
            else
                cout << (3 * (++j)) - p[i] << " ";
            j++;
        }
        cout << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
