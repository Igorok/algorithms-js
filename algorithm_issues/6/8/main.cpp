/*
Output format. The largest number that can be composed out of a[1], ..., a[n].

Sample Input 1:
3
23 39 92
Sample Output 1:
923923

Sample Input 2:
2
21 2
Sample Output 2:
221
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using std::vector;
using std::string;


struct great_price
{
    inline bool operator() (const string a, const string b)
    {
        return a + b > b + a;
    }
};

string getNumber (vector<string> &numList) {
    std::sort(numList.begin(), numList.end(), great_price());
    string num = "";

    for (int i = 0; i < numList.size(); ++i) {
        num += numList[i];
    }
    return num;
}

int main () {
    int n;
    std::cin >> n;

    vector<string> numList;

    for (int i = 0; i < n; ++i) {
        string val;
        std::cin >> val;
        numList.push_back(val);
    }
    std::cout << getNumber(numList) << "\n";

    return 0;
}
