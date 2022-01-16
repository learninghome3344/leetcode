/*
 * @lc app=leetcode.cn id=67 lang=cpp
 *
 * [67] 二进制求和
 */

// @lc code=start
class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0;
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());

        int i = 0, j = 0;
        string res;
        while (i < a.length() || j < b.length() || carry > 0) {
            int ia = i >= a.length() ? 0 : (a[i] - '0');
            int ib = j >= b.length() ? 0 : (b[i] - '0');
            res += char((ia + ib + carry) % 2 + 48);
            carry = (ia + ib + carry) / 2;
            ++i; 
            ++j;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
// @lc code=end

