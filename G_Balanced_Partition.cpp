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

void solve()
{
    int n;
    cin >> n;
    vector<int> prefix(n);
    vector<int> suffix(n + 1);
    vector<int> a(n);
    cin >> a[0];
    prefix[0] = a[0];
    forn(1, n)
    {
        cin >> a[i];
        prefix[i] = prefix[i - 1] + a[i];
    }
    suffix[n] = 0;
    forr(n - 1, 0)
    {
        suffix[i] = suffix[i + 1] + a[i];
    }
    if (n == 1)
        cout << 0 << endl;
    else
    {
        int cnt = 0;
        int zcnt = 0;
        forn(0, n)
        {
            if (prefix[i] == suffix[i + 1])
            {
                if (prefix[i] != 0)
                {
                    cnt += 1;
                    zcnt = 0;
                }
                else
                {
                    zcnt++;
                    if (zcnt != 2)
                    {
                        cnt += 1;
                    }
                }
            }
        }
        // cnt+= (zcnt/2);
        cout << cnt << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
