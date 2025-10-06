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
    int t;
    cin >> t;
    while (t--)
    {
        int n; cin>>n; 
        int cnt=0; 
        vector<int>a(n); 
        // map<int, bool> chck; 
        forn(0, n) {
            cin >> a[i]; 
            // chck[a[i]] = true; 
        }
        sort(all(a)); 
        int strt = a[0]; 
        forn(1, n){
            if(abs(strt-a[i])<=1 && abs(strt-a[i])>0) {
                if(cnt==0)cnt+=2; 
                else cnt++; 
            }
            else strt = a[i] ; 
        }
        
        cout<<cnt<<endl; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
