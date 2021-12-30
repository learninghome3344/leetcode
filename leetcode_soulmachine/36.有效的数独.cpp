/*
 * @lc app=leetcode.cn id=36 lang=cpp
 *
 * [36] 有效的数独
 */

// @lc code=start
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> row(9, vector<int>(10, 0));
        vector<vector<int>> col(9, vector<int>(10, 0));
        vector<vector<int>> grid(9, vector<int>(10, 0));

        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] == '.') continue;
                int n = board[i][j] - '0';
                int k = (i / 3) * 3 + j / 3;
                row[i][n]++;
                col[j][n]++;
                grid[k][n]++;
                if (row[i][n] > 1 || col[j][n] > 1 || grid[k][n] > 1) {
                    return false;
                }
            }
        }
        return true;
    }
};
// @lc code=end

