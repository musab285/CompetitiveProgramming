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
#define all(x) x.begin(), x.end()

bool isSortedasc(vector<int> &arr)
{
    for (int i = 0; i < arr.size() - 1; i++)
    {
        if (arr[i] > arr[i + 1])
            return false;
    }
    return true;
}

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
        if (isSortedasc(arr)){
            cout<<0<<endl;
        }
        else{
            int cnt = 0;
            while(!isSortedasc(arr)){
                if(mni<mxi && mxi!=n-1){
                    sort(arr.begin()+1, arr.end());
                    mxi=n-1;} 
                else{
                    sort(arr.begin(), arr.end()-1);
                    mni=0;}
                cnt++;
            }
            cout<<cnt<<endl;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
