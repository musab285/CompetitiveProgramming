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
    ll t;
    cin >> t;
    while (t--)
    {
        ll n, s, m;
        cin>>n>>s>>m; 
        vector<bool>chck(m, true);
        forn(0, n){
            ll l, r;
            cin>>l>>r; 
            forn(l-1, r){
                chck[i] = false; 
            }
        }
        bool otflg = true;
        for(int i = 0; i<m&&otflg; i++){
            bool flg = true;
            for(int j = 0; j<s&&flg;j++ ){
                if(!chck[j]){
                    flg = false; 
                }
            }
            cout<<yn(flg)<<endl; 
            otflg = flg; 
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
