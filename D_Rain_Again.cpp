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
    ll t;
    cin >> t;
    while (t--)
    {
        ll n, k; cin>>n>>k;
        vector<ll>a(n); 
        forn(0, n){
            cin>>a[i]; 
        }
        ll i = 0; 
        ll up = n/k;
        cout<<up<<endl; 
        ll mn=LLONG_MIN; 
        while(i<n){
            mn = max(mn, (a[i+(up-1)]-a[i])); 
            i+=up; 
        }
        cout<<mn<<endl; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
