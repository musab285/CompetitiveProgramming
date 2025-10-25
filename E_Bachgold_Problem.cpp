#include<iostream>
using namespace std; 

int main(){
    int x; cin>>x; 
    int cnt;
    if(x%2!=0){
        cnt = (x-3)/2; 
        cout<<cnt+1<<endl; 
        for(int i=0; i<cnt; i++) cout<<2<<" "; 
        cout<<3<<endl; 
    }
    else{
        cnt = x/2; 
        cout<<cnt<<endl; 
        for(int i=0; i<cnt; i++) cout<<2<<" "; 
        cout<<endl; 
    }
}