/*
 * @lc app=leetcode.cn id=128 lang=cpp
 *
 * [128] 最长连续序列
 */

// @lc code=start
// [100,4,200,1,3,2]
class Solution {
public:
    // 维护一个map，记录当前元素所属序列的长度
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();

        unordered_map<int, int> map;
        int res = 0;
        for (auto i: nums) {
            if (map.find(i) != map.end()) continue;
            int left = 0, right = 0;
            if (map.find(i-1) != map.end()) left = map[i-1];
            if (map.find(i+1) != map.end()) right = map[i+1];
            int cur = left + right + 1;
            res = max(res, cur);
            map[i] = cur;
            map[i-left] = cur;
            map[i+right] = cur;
        }
        return res;
    }
    /*
    // 维护一个map，记录遍历到的item是否使用过，保证每个元素只使用一次
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();

        unordered_map<int, bool> used;
        for (auto i: nums) {
            used[i] = false;
        }

        int res = 0;
        for (auto i: nums) {
            if (used[i]) continue;
            used[i] = true;
            int cur = 1;
            for (int j = i + 1; used.find(j) != used.end(); ++j) {
                used[j] = true;
                ++cur;
            }
            for (int j = i - 1; used.find(j) != used.end(); --j) {
                used[j] = true;
                ++cur;
            }
            res = max(res, cur);
        }
        return res;
    }
    */
};
// @lc code=end

