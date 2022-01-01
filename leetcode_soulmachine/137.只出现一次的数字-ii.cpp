/*
 * @lc app=leetcode.cn id=137 lang=cpp
 *
 * [137] 只出现一次的数字 II
 */

// @lc code=start
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int> counts(32, 0);
        for (auto n: nums) {
            for (int i = 0; i < 32; ++i) {
                counts[i] += n & 1;
                n >>= 1;
            }
        }
        int res = 0;
        for (int i = 0; i < 32; ++i) {
            res <<= 1;
            res |= counts[31-i] % 3;
        }
        return res;
    }
};
// @lc code=end

