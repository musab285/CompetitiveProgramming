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
    ll n;
    cin >> n;
    vector<ll> arr(n - 1);
    ll sum = 0;
    forn(0, n - 1)
    {
        cin >> arr[i];
        sum += arr[i];
    }
    ll actsm = (n * (n + 1)) / 2;
    cout << actsm - sum << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
