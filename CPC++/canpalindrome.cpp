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
    ll t;
    cin >> t;
    while (t--)
    {
        ll k, n;
        map<char, ll>hsh; 
        cin>>n>>k; 
        char x;
        forn(0,n){
            cin>>x;
            hsh[x]++; 
        }
        ll rm = n-k;
        ll cnt = 0;
        bool flg = true; 
        for(const auto &y : hsh){
            if(y.second%2==0){
                cnt++;
            }
            else if(flg){
                flg = false; 
                cnt++; 
            }
        }
        cout<<yn(cnt>=rm)<<endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
