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
        ll n, m;
        cin >> n >> m;
        int prv = 0;
        ll prm = 0;
        ll cnt = 0;
        forn(0, n)
        {
            int a, b;
            cin >> a >> b;
            if ((a - prm) % 2 == 0)
            {
                if (prv == b)
                {
                    cnt += (a - prm);
                }
                else
                {
                    cnt += (a - prm - 1);
                }
            }
            else
            {
                if (prv != b)
                {
                    cnt += (a - prm);
                }
                else
                {
                    cnt += (a - prm - 1);
                }
            }
            prm = a;
            prv = b;
        }
        cnt += (m-prm);
        cout << cnt << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
