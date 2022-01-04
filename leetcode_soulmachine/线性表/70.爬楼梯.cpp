/*
 * @lc app=leetcode.cn id=70 lang=cpp
 *
 * [70] 爬楼梯
 */

// @lc code=start
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int pre = 1, cur = 2;
        for (int i = 3; i <= n; ++i) {
            int tmp = pre + cur;
            pre = cur;
            cur = tmp;
        }
        return cur;
    }
};
// @lc code=end

