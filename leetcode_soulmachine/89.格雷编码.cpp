/*
 * @lc app=leetcode.cn id=89 lang=cpp
 *
 * [89] 格雷编码
 */

// @lc code=start
class Solution {
public:
    /*
    0, 1 -> 00, 01, 11, 10
    *) add '0' to every element of the seq, 00, 01
    *) add '1' to every element of the reversed seq, (1, 0 -> 11, 10)
    *) merge the result: 00, 01, 11, 10
    */
    vector<int> grayCode(int n) {
        vector<int> res = {0};
        int head = 1;
        for (int i = 0; i < n; ++i) {
            int size = res.size();
            for (int j = size-1; j >= 0; --j) {
                res.push_back(head + res[j]);
            }
            head <<= 1;
        }
        return res;
    }
};
// @lc code=end

