/*
 * @lc app=leetcode.cn id=31 lang=cpp
 *
 * [31] 下一个排列
 */

// @lc code=start
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int partition = -1;
        for (int i = nums.size()-1; i > 0; --i) {
            if (nums[i] > nums[i-1]) {
                partition = i-1;
                break;
            }
        }
        if (partition == -1) {
            reverse(nums.begin(), nums.end());
            return;
        }
        int change = partition;
        for (int i = nums.size()-1; i > partition; --i) {
            if (nums[i] > nums[partition]) {
                int tmp = nums[i];
                nums[i] = nums[partition];
                nums[partition] = tmp;
                break;
            }
        }
        reverse(nums.begin()+partition+1, nums.end());
    }
};
// @lc code=end

