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
        map<int, int>chck; 
        int n; cin>>n; 
        vector<int>x(n); 
        forn(0, n){
            cin>>x[i]; 
            chck[x[i]]++; 
        }
        int mn = n; 
        for(const auto& x: chck){
            mn=min(mn, x.second); 
        }
        int cnt=0; 
        for(const auto& x: chck){
            if(x.second>mn){
                cnt+=(x.second-mn); 
                cnt = min(cnt, x.second); 
            }
        }
        cout<<n-cnt<<endl; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
