/*
 * @lc app=leetcode.cn id=134 lang=cpp
 *
 * [134] 加油站
 */

// @lc code=start
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int start = 0, size = gas.size();
        while (start < size) {
            int cur_gas = 0, cur_cost = 0, end = 0;
            for (int i = 0; i < size; ++i) {
                cur_gas += gas[(start + i) % size];
                cur_cost += cost[(start + i) % size];
                end = i;
                if (cur_gas < cur_cost) {
                    start += i + 1;
                    break;
                }
            }
            if (end == size - 1 && cur_gas >= cur_cost) {
                return start % size;
            }
        }
        return -1;
    }
};
// @lc code=end

