/*
 * @lc app=leetcode.cn id=8 lang=cpp
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
class Solution {
public:
    int myAtoi(string s) {
        int sign = 1;
        int i = 0;
        const int n = s.length();
        while (i < n && s[i] == ' ') {
            ++i;
        }
        if (i < n && (s[i] == '-' || s[i] == '+')) {
            if (s[i] == '-') {
                sign = -1;
            }
            ++i;
        }

        int result = 0;
        while (i < n) {
            if (s[i] < '0' || s[i] > '9') {
                break;
            }
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && (s[i] - '0') > INT_MAX % 10)) {
                return sign == - 1 ? INT_MIN: INT_MAX;
            }
            result = 10 * result + (s[i] - '0');
            ++i;
        }
        return sign * result;
    }
};
// @lc code=end

