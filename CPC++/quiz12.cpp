#include <bits/stdc++.h>
using namespace std;

int search(vector<int> nums, int target)
{
    int left = 0, right = nums.size();
    int ix;
    while (left <= right)
    {
        int mid = left + ((right - left) / 2);
        if (target == nums[mid])
        {
            ix = mid;
            while (nums[ix - 1] == target)
            {
                ix--;
            }
            break;
        }
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return ix;
}

int main()
{
    cout << search({1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 9}, 5);
}