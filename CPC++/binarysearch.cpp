#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> nums = {-1, 0, 3, 5, 9, 12};
    int target = 2;
    int left = 0;
    int right = nums.size()-1;
    // cout<<right;
    bool flg = false;
    int ix; 
    int mid = 1 + (right - left)/2;
    while (left!=right && not flg){
        // cout<<mid;
        if(nums[mid]>target){
            right = mid-1;
            mid = 1 + (right - left)/2;
        }
        else if(nums[mid]<target){
            left = mid+1;
            mid += 1 + (right - left)/2;
        }
        else{
            flg = true; 
            ix = mid; 
        }
    }
    if (flg){
        cout<< ix;
    }else{
        cout<< -1;
    }
}