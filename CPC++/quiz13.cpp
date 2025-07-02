#include <bits/stdc++.h>
using namespace std;

void selectionSort(vector<int> &nums)
{
    for (int right = nums.size() - 1; right > 0; right--)
    {
        int mx = nums[right];
        int mxi;
        for (int left = right - 1; left >= 0; left--)
        {
            if (nums[left] > mx)
            {
                mx = nums[left];
                mxi = left;
            }
        }
        swap(nums[right], nums[mxi]);
    }
    for (int i : nums)
    {
        cout << i << " ";
    }
}

// no effect on time complexity of selection sort as the algo runs for the same number of time

int main()
{
    vector<int> nums = {2, 3, 1, 4, 5, 0};
    selectionSort(nums);
}
