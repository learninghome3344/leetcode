/*
 * @lc app=leetcode.cn id=135 lang=cpp
 *
 * [135] 分发糖果
 */

// @lc code=start
class Solution {
public:
    int candy(vector<int>& ratings) {
        int size = ratings.size();
        vector<int> candy(size, 1);
        
        for (int i = 1; i < size; ++i) {
            if (ratings[i] > ratings[i-1]) {
                candy[i] = candy[i-1] + 1;
            }
        }

        for (int i = size-2; i >= 0; --i) {
            if (ratings[i] > ratings[i+1]) {
                candy[i] = max(candy[i+1] + 1, candy[i]);
            }
        }

        return accumulate(candy.begin(), candy.end(), 0);
    }
};
// @lc code=end

