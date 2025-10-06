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

ll Fib(ll n){
    if (n <= 1)
        return n;
    vector<int> dp(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    for (ll i = 2; i <= n; ++i){
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

void solve()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll x; cin>>x; 
        cout<<Fib(x+1)%10<<endl; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
