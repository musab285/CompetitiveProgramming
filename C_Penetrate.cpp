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
    string s;
    while (cin>>s) {
        int lc = 0, uc=0, nc=0; 
        int cnt = 0; 
        forn(0, s.length()){
            if(s[i]>='a' && s[i]<='z'){
                lc++;
            }
            else if(s[i]>='A' && s[i]<='Z'){
                uc++; 
            }
            else{
                nc++; 
            }
            if(lc>=1 && nc>=1 && uc>=1){ cnt++; lc=0; uc=0; nc=0; }
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
