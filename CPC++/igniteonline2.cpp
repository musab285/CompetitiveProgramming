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
#define bohotbara INT_MAX
#define bohotchota INT_MIN

void solve()
{
    int n;
    double r;
    double ans;
    cin >> n;
    cin >> r;
    vector<double> x(n);
    vector<double> y(n);
    bool xallng = true;
    bool xallps = true;
    bool yallng = true;
    bool yallps = true;
    for (int i = 0; i < n; i++)
    {
        cin >> x[i] >> y[i];
        if (x[i] + r >= 0)
            xallng = false;
        if (x[i] + r <= 0)
            xallps = false;
        if (y[i] + r >= 0)
            yallng = false;
        if (y[i] + r <= 0)
            yallps = false;
    }
    if (xallng || yallng || xallps || yallps)
    {
        ans = 180.000000;
        cout << "UYES";
    }
    else
    {
        int mxy = bohotchota;
        double m1, m2;
        forn(0, n)
        {
            for (int j = i; j < n; j++)
            {
                if (mxy < abs(y[i] - y[j]))
                {
                    mxy = abs(y[i] - y[j]);
                    m1 = (y[i] - 0) / (x[i] - 0);
                    m2 = (y[j] - 0) / (x[j] - 0);
                }
            }
        }
        ans = atan(abs((m1 - m2) / (1 + (m1 * m2))));
    }
    cout << ans << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
