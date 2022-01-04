/*
 * @lc app=leetcode.cn id=80 lang=cpp
 *
 * [80] 删除有序数组中的重复项 II
 */

// @lc code=start
// #include <iostream>
// #include <vector>
// using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 3) return nums.size();
        int index = 2;
        for (int i = 2; i < nums.size(); i++) {
            if (nums[i] != nums[index-2]) {
                nums[index++] = nums[i];
            }
        }
        return index;
    }
};

// int main() {
//     auto s = Solution();
//     vector<int> nums = {1,1,1,2,2,2,3};
//     int index = s.removeDuplicates(nums);
//     for (int i = 0; i <= index; i++) {
//         cout << nums[i] << " ";
//     }
// }



// @lc code=end

