#include<iostream>
#include<vector>
#include<string>
#include <algorithm>

using std::string;
using std::vector;

class Solution {

public:
    string reverseParentheses(string s) {
        vector<int>open;
        string output;

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                open.push_back(output.size());
            } else if (s[i] == ')') {
                int start = open.back();
                open.pop_back();
                std::reverse(output.begin() + start, output.end());
            } else {
                output.push_back(s[i]);
            }
        }
        return output;
    }
};

void test () {
    string input = "(ed(et(oc))el)";
    Solution* sol = new Solution();
    string output = sol->reverseParentheses(input);

    std::cout << output << "\n";
}

int main () {
    test();

    return 0;
}
