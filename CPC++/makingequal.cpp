#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define forn(a, b) for (int i = a; i < b; i++)
// #define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bohotbara INT_MAX
#define bohotchota INT_MIN

void solve()
{
    ll n;
    cin >> n;
    vector<int> arr(n);
    forn(0, n)
    {
        cin >> arr[i];
    }
    ll cnt = 0;
    for (int i = n; i > 0; i--)
    {
        if (arr[i] < arr[i - 1])
        {
            cnt += abs(arr[i] - arr[i - 1]);
        }
    }
    cout << cnt << " ";
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
