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
    int n, k;
    cin >> n >> k;
    map<char, int> chck;
    map<char, int> chck2;
    string s;
    cin >> s;
    forn(0, n){
        chck[s[i]]++; 
        chck2[s[i]]++; 
    }
    set<char>a; 
    k--; 
    forn(0, n)
    {
        chck[s[i]]--; 
        a.insert(s[i]); 
        if(chck[s[i]]==0){
            a.erase(s[i]); 
            k+=chck2[s[i]]; 
        }
        if(a.size()>1){
            k--; 
        }
        if(k<0){
            cout<<"YES"<<endl; 
            return; 
        }
    } 
    cout << "NO" << endl;
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
