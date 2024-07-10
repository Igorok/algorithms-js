#include <iostream>
#include <string>
#include <vector>
#include <map>



int main()
{
	std::string inputStr;
	std::getline(std::cin, inputStr);

	std::map <std::string, int>countStr;

    for (int i = 0; i < inputStr.size() - 1; ++i) {
        char first = inputStr[i];
        char second = inputStr[i + 1];

        if (first != ' ' && second != ' ') {
            std::string val = std::string{first, second};

            if (auto search = countStr.find(val); search != countStr.end()) {
                countStr[val] += 1;
            } else {
                countStr[val] = 1;
            }
        }
    }

    int maxCount = 0;
    std::string maxVal;

    for (auto const& x : countStr)
    {
        if (x.second > maxCount) {
            maxVal = x.first;
            maxCount = x.second;
        } else if (maxCount == x.second) {
            maxCount = x.second;
            maxVal = x.first > maxVal ? x.first : maxVal;
        }
    }

    std::cout << maxVal << "\n";

	return 0;
}
