/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        if (nums.size() < 4 || nums[0] >= 1000000000) return res;
        sort(nums.begin(), nums.end());

        auto last = nums.end();
        for (auto i = nums.begin(); i < last - 3; ++i) {
            if (i > nums.begin() && *i == *(i-1)) continue;
            for (auto j = i+1; j < last - 2; ++j) {
                if (j > i+1 && *j == *(j-1)) continue;
                auto l = j+1, r = last-1;
                while (l < r) {
                    if ((long)(*i) + *j + *l + *r == target) {
                        res.push_back({*i, *j, *l, *r});
                        ++l;
                        --r;
                        while (l < r && *l == *(l-1)) {
                            ++l;
                        }
                        while (l < r && *r == *(r+1)) {
                            --r;
                        }
                    } else if ((long)(*i) + *j + *l + *r < target) {
                        ++l;
                    } else {
                        --r;
                    }
                }
            }
        }
        return res;
    }
};
// @lc code=end

