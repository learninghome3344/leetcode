// Œ¥≤Œº”£¨¡∑¡∑ ÷

class Solution2129 {
public:
    bool isSameAfterReversals(int num) {
        return(num == 0) || (num % 10 != 0);
    }
};

class Solution2120 {
public:
    vector<int> executeInstructions(int n, vector<int>& startPos, string s) {
        vector<int> res;
        for (int start = 0; start < s.size(); ++start) {
            int x = startPos[0], y = startPos[1], count = 0;
            for (int i = start; i < s.size(); ++i) {
                // cout << "start_index=" << start << " ";
                // cout << "i=" << i << " curPos[0]=" << x << " curPos[1]=" << y << " ";
                if (s[i] == 'L') --y;
                else if (s[i] == 'R') ++y;
                else if (s[i] == 'U') --x;
                else if (s[i] == 'D') ++x;                
                // cout << " newPos[0]=" << x << " newPos[1]=" << y << endl;
                if (x < 0 || x >= n || y < 0 || y >= n) break;
                ++count;
            }
            res.push_back(count);
        }
        
        return res;
    }
};