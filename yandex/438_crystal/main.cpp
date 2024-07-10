#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using std::vector;

int main()
{
	std::vector<std::string> sarr;
	std::string word;
	while (std::cin >> word) {
		sarr.push_back(word);
	}

    std::cout
        << " first " << sarr[0]
        << " second " << sarr[1]
        << " third " << sarr[2]
        << "\n";

    std::string result;

    vector<vector<int>> sizes;
    for (int i = 0; i < 3; ++i) {
        sizes.push_back(vector<int>{ 0, sarr[i].size() });
    }

    while (
        sizes[0][0] < sizes[0][1]
        && sizes[1][0] < sizes[1][1]
        && sizes[2][0] < sizes[2][1]
    ) {
        std::cout
        << " 1 " << sarr[0][sizes[0][0]]
        << " 2 " << sarr[1][sizes[1][0]]
        << " 3 " << sarr[2][sizes[2][0]]
        << "\n";

        std::cout
        << " 1 " << sizes[0][0]
        << " 2 " << sizes[1][0]
        << " 3 " << sizes[2][0]
        << "\n";


        if (
            sarr[0][sizes[0][0]] != sarr[1][sizes[1][0]]
            || sarr[1][sizes[1][0]] != sarr[2][sizes[2][0]]
        ) break;


        char letter = sarr[0][sizes[0][0]];

        std::cout
        << " letter " << letter
        << "\n";

        vector<int> length(3, 0);

        for (int i = 0; i < 3; ++i) {
            while (
                sizes[i][0] < sizes[i][1]
            ) {
                sizes[i][0] += 1;
                length[i] += 1;

                if (sarr[i][sizes[i][0]] != sarr[i][sizes[i][0]-1]) {
                    break;
                }
            }
        }

        /*
        int sum = 0;
        for (int i = 0; i < 3; ++i) {
            sum += length[i];
        }
        int middle = (int) sum / 3;
        */
        std::sort(length.begin(), length.end(),std::greater<int>());
        int middle = length[1];

        std::cout
        << " middle " << middle
        << "\n";

        result += std::string(middle, letter);


        std::cout
        << " std::string(middle, letter) " << std::string(middle, letter)
        << " result " << result
        << "\n";

    }

    if (
        sizes[0][0] != sizes[0][1]
        || sizes[1][0] != sizes[1][1]
        || sizes[2][0] != sizes[2][1]
    ) {
        std::cout << "IMPOSSIBLE" << "\n";
    } else {
        std::cout << result << "\n";
    }

	return 0;
}










/*

aaaza
aazzaa
azzza

aaaza
aazzaa
azzzaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


aaaaaa
aaaaa
a

aaa

10
1



*/
