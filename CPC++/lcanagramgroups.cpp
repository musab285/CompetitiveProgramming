#include <bits/stdc++.h>
#include <string.h>
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

bool isAnagram(string s, string t) {
        if(s.size()!=t.size())return false;
        unordered_map<char, int> frqs; 
        unordered_map<char, int> frqt;
        for(int i = 0; i<s.size(); i++){
            frqs[s[i]]++;
            frqt[t[i]]++;  
        }
        for(char x : s){
            if(frqs[x]!=frqt[x]){
                return false; 
            }
        }
        return true;}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<str> strs = {"eat","tea","tan","ate","nat","bat"};
    vector<vector<string>> ans; 
    while(strs.size()>0){
        str prv = strs[0]; 
        vector<string> nw = {prv}; 
        swap(strs[0], strs[strs.size()-1]);
        strs.pop_back(); 
        size_t i = 0; 
        while(i<strs.size()){
            if(isAnagram(prv, strs[i])){
                nw.push_back(strs[i]); 
                swap(strs[i], strs[strs.size()-1]);
                strs.pop_back();
            }else{
                i++; 
            }
        }
        ans.push_back(nw); 
        // cnt++;
    }
    for(vector<str> &p : ans){
        for(str s : p){
            cout<<s<<" ";
        }
        cout<<endl;
    }
}
