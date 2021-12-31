/*
 * @lc app=leetcode.cn id=48 lang=cpp
 *
 * [48] 旋转图像
 */

// @lc code=start
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.empty()) return;
        int size = matrix.size();
        int tmp;
        for (int i = 0; i < size / 2; ++i) {
            for (int j = 0; j < (size + 1) / 2; ++ j) {
                tmp = matrix[i][j];
                swap(matrix[i][j], matrix[size-j-1][i]);
                swap(matrix[size-j-1][i], matrix[size-i-1][size-j-1]);
                swap(matrix[size-i-1][size-j-1], matrix[j][size-i-1]);
                swap(matrix[j][size-i-1], tmp);
            }
        }
    }
};
// @lc code=end

