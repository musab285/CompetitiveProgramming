#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define str string
#define forn(a, b) for (int i = a; i < b; i++)
#define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bohotbara INT_MAX
#define bohotchota INT_MIN

void solve()
{
    int t;
    cin >> t;
    while (t--)
    {
        int k, n;
        cin >> k >> n;
        vector<int> a(n);
        forn(0, n)
        {
            cin >> a[i];
        }
        ll prft = 0;
        int i = 0;
        while (i < n && k > 0)
        {
            int mx = bohotchota;
            int j = i + 1;
            int mxi;
            while (j < n && (n - j) >= (k - 1) * 2)
            {
                mx = max(mx, a[j] - a[i]);
                if (mx == a[j])
                {
                    mxi = j;
                }
                cout << mx <<" "<< j<<" "<<i << endl;
                j++;
                // cout << j << endl;
            }
            k--;
            i = mxi;
            prft += mx;
        }
        cout << prft << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
