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
    int n;
    cin >> n; 
    vector<int> x(n);
    forn(0, n) cin >> x[i];
    sort(x.begin(), x.end()); 
    int q ; cin>>q; 
    forn(0, q){
        int y; cin>>y; 
        int lw = 0,  hg = n-1;
        int ans=-1; 
        while(lw<=hg){
            int md = (lw+hg)/2; 
            if(x[md]>y){
                hg = md-1; 
            }
            else{
                ans = md; 
                lw = md+1; 
            }
        }
        cout<<ans+1<<endl; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
