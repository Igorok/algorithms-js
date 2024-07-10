#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using std::vector;

struct great_priority
{
    inline bool operator() (const vector<int>& a, const vector<int>& b)
    {
        if (a[1] == b[1])
            return a[0] < b[0];
        return a[1] > b[1];
    }
};



int main()
{
    int n;
    std::cin >> n;

    long long maxStress = 0;
    int daysLimit = 0;
    vector<vector<int>> days;

    for (int i = 0; i < n; ++i) {
        int d, w;
        std::cin >> d >> w;
        days.push_back(vector<int>{d, w});

        if (d > daysLimit) daysLimit = d;
        maxStress += w;
    }

    std::sort(days.begin(), days.end(), great_priority());

    vector<int> work(daysLimit + 1, -1);
    int lower = 0;
    int top = work.size() - 1;

    for (int i = 0; i < n; ++i) {
        int d = days[i][0];
        int w = days[i][1];

        int start = d;
        if (d >= top) start = top;

        for (int j = start; j > lower; --j) {
            if (work[j] == -1) {
                work[j] = w;
                maxStress -= w;
                daysLimit -= 1;

                if (j == lower + 1) lower += 1;
                if (d >= top) top = j - 1;
                break;
            }
        }


        if (daysLimit == 0) {
            break;
        }
    }

    std::cout << maxStress <<"\n";

	return 0;
}
