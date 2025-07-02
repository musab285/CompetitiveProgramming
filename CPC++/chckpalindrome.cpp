#include <bits/stdc++.h>
using namespace std;

bool chckpalindrome(string s, int left, int right)
{
    if (left == right)
    {
        return true;
    }
    if (s[left] == s[right])
    {
        return chckpalindrome(s, ++left, --right);
    }
    else
    {
        return false;
    }
}

int main()
{
    string s = "racecar"; 
    
    if(chckpalindrome(s, 0, s.length()-1))
        cout<<"YES";
    else
        cout<<"NO"; 
}