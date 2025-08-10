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

// bool isSortedasc(vector<int> &arr)
// {
//     for (int i = 0; i < arr.size() - 1; i++)
//     {
//         if (arr[i] > arr[i + 1])
//             return false;
//     }
//     return true;
// }

void solve()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll k, n;
        cin >> n >> k;
        string s;
        cin >> s;
        ll zr = 0;
        forn(0, n)
        {
            if (s[i] == '0')
                zr++;
        }
        ll ans;
        if (zr % k != 0)
            ans = (zr / k) + 1;
        else
            ans = zr / k;

        if (n % k != 0)
            ans += (n / k) + 1;
        else
            ans += n / k;
        cout <<ans << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
