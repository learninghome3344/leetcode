/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
public:
    // 后续补充最小栈的方法
    // 先为每个元素分别找到左边和右边最高的柱子
    int trap(vector<int>& height) {
        int size = height.size();
        vector<int> max_left(size, 0), max_right(size, 0);
        for (int i = 1; i < size; ++i) {
            max_left[i] = max(max_left[i-1], height[i-1]);
        }
        for (int i = size-2; i >= 0; --i) {
            max_right[i] = max(max_right[i+1], height[i+1]);
        }

        int res = 0;
        for (int i = 0; i < size; ++i) {
            int h = min(max_left[i], max_right[i]) - height[i];
            res += max(h, 0);
        }
        return res;
    }
};
// @lc code=end

