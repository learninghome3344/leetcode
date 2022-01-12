/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] 验证回文串
 */

// @lc code=start
#include <iostream>
using namespace std;
#include <algorithm>


class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        auto left = s.begin();
        auto right = prev(s.end());
        while (left < right) {
            if (!::isalnum(*left)) ++left;
            else if (!::isalnum(*right)) --right;
            else if (*left != *right) return false;
            else {
                ++left;
                --right;
            }
        }
        return true;
    }
};

// int main() {
//     Solution s;
//     cout << (s.isPalindrome("aa") == true? "true": "false");
// }
// @lc code=end

