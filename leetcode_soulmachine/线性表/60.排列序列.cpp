/*
 * @lc app=leetcode.cn id=60 lang=cpp
 *
 * [60] 排列序列
 */

// @lc code=start
// https://blog.csdn.net/ZIFENGCHUANSHUO007/article/details/38902123
class Solution {
public:
    string getPermutation(int n, int k) {
        string s(n, '0');
        for (int i = 0; i < n; ++i) {
            s[i] += i+1;
        }
        return kthPermution(s, k);
    }

private:
    int factorial(int n) {
        int res = 1;
        for (int i = 1; i <= n; ++i) {
            res *= i;
        }
        return res;
    }

    template<typename Sequence>
    Sequence kthPermution(Sequence s, int k) {
        Sequence str(s);
        Sequence res;
        int n = str.size();
        --k;
        int base = factorial(n-1);
        for (int i = n-1; i > 0; --i) {
            auto tmp = next(str.begin(), k / base);
            res.push_back(*tmp);
            str.erase(tmp);
            k %= base;
            base /= i;
        }
        res.push_back(str[0]);
        return res;
        
    }
};
// @lc code=end

