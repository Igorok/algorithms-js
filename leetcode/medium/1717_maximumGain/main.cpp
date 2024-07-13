/*
Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

---

cdbcbbaaabab
ba ba

cdbcbaab

ba ab

cdbc

5+5+5+4

---

aabbaaxybbaabb

ab ab

abaaxybbab

abaaxybbab

ab ab

aaxybb

5+5+5+5
*/

#include<iostream>
#include<string>
#include<vector>

using std::string;
using std::vector;

class Solution {
int x;
int y;
int gain;
string remainder;

bool checkX (char a, char b) {
    return (a == 'a' && b == 'b');
}
bool checkY (char a, char b) {
    return (a == 'b' && b == 'a');
}
void findAB (char check) {
    if (this->remainder.size() < 2) return;

    string remainder = "";

    for (int i = 0; i < this->remainder.size(); ++i) {
        if (remainder.size() == 0) {
            remainder.push_back(this->remainder[i]);
            continue;
        }
        char a = remainder.back();
        char b = this->remainder[i];

        if (check == 'x' && this->checkX(a, b)) {
            remainder.pop_back();
            this->gain += this->x;
        } else if (check == 'y' && this->checkY(a, b)) {
            remainder.pop_back();
            this->gain += this->y;
        } else {
            remainder.push_back(this->remainder[i]);
        }
    }

    this->remainder = remainder;
}

public:
    int maximumGain(string s, int x, int y) {
        this->gain = 0;
        this->remainder = s;
        this->x = x;
        this->y = y;

        if (x > y) {
            this->findAB('x');
            this->findAB('y');
        } else {
            this->findAB('y');
            this->findAB('x');
        }

        return this->gain;
    }
};

void test () {
    Solution* solution = new Solution();

    int result = solution->maximumGain("cdbcbbaaabab", 4, 5);
    std::cout << ((result != 19) ? "Error " : "Success ") << result << "\n";

    result = solution->maximumGain("aabbaaxybbaabb", 5, 4);
    std::cout << ((result != 20) ? "Error " : "Success ") << result << "\n";


    result = solution->maximumGain("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", 5, 4);
    std::cout << ((result != 210) ? "Error " : "Success ") << result << "\n";
}




















int main () {
    test();
    return 0;
}
