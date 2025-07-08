#include <bits/stdc++.h>
#include <algorithm>
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

void solve()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n; 
        cin >> n;
        vector<int> arr(n);
        int mx = chota;
        int mn = bara;
        int mni, mxi; 
        forn(0, n){
            cin>>arr[i];
            mx = max(arr[i], mx);
            if(mx==arr[i]) mxi = i;
            mn = min(arr[i], mn);
            if(mn==arr[i]) mni = i;
        }
        bool flg = false;
        int i = 0;
        while( !flg && i<n-1){
            if(arr[i] > arr[i+1]){
                flg = true;
            }
            i++;
        } 
        if (!flg){
            cout<<0<<endl;
            ;
        }

        else if(mxi==n-1 || mni==0){   
            cout<<1<<endl;
        }
        else if(mni> mxi){
            cout<<3<<endl;
        }else{
            cout<<2<<endl;
        } 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
