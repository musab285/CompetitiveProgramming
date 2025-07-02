#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define for(a, b) for (int i = a; i < b; i++)
#define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bohotbara INT_MAX
#define bohotchota INT_MIN

void solve()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        vector<ll> a(n);
        vector<ll> b;
        ll mn = 0;
        for (0, n)
        {
            cin>>a[i];
        }
        sort(a.begin(), a.end());
        // for (0, n)
        // {
        //     cout<<a[i]<<" ";
        // }
        if (n%2){
            a.pb(0);
        }
        for(0,n){
            b.pb(a[i]+a[i+1]);
            i++;
        }
        ll i = 0;
        ll prv = -1; 
        ll sz = b.size();
        for(0, sz){
            cout<<b[i]<<" ";
        }
        // while(i < sz){
        //     // cout<<b[i]<<" "<<mn<<endl;
        //     if (b[i]!=prv && b[i]==mn){
        //         mn++;
        //     }
        //     prv = b[i];
        //     i++;
        // }
        // cout<<mn<<endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
