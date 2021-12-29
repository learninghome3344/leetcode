/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() < 3) return res;
        sort(nums.begin(), nums.end());

        auto last = nums.end();
        for (auto i = nums.begin(); i < last - 2; ++i) {
            // a is i, find b&c between i+1 ~ last-1
            if (i > nums.begin() && *i == *(i-1)) continue;
            auto j = i+1, k = last-1;
            while (j < k) {
                int tmp = *i + *j + *k;
                if (tmp == 0) {
                    res.push_back({*i, *j, *k});
                    ++j;
                    --k;
                    while (*j == *(j-1) && j < k) ++j;
                    while (*k == *(k+1) && j < k) --k;
                } else if (tmp > 0) {
                    --k;
                } else {
                    ++j;
                }
            }
        }
        return res;
    }
};
// @lc code=end

