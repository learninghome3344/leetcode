/*
 * @lc app=leetcode.cn id=16 lang=cpp
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if (nums.size() < 3) return -1;
        sort(nums.begin(), nums.end());
        int res = nums[0] + nums[1] + nums[2];
        
        auto last = nums.end();
        for (auto i = nums.begin(); i < last-2; ++i) {
            auto j = i+1, k = last-1;
            while (j < k) {
                int tmp = *i + *j + *k;
                if (abs(tmp - target) < abs(res - target)) {
                    res = tmp;
                }
                if (tmp < target) {
                    ++j;
                } else {
                    --k;
                }
            }
        }
        return res;
    }
};
// @lc code=end

