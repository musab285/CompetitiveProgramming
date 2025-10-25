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
    int t;
    cin >> t;
    while (t--)
    {
        int mx = 1; 
        int x; cin>>x; 
        int lft = 1; 
        while(lft<x){
            mx = max(mx, __gcd(lft, x));
            x--; lft++;
        }
        cout<<mx<<endl; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
