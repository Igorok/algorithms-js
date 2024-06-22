/*
Input format.
The first line contains the number of points n. Each of the following n lines defines a point (x[i] , y[i]).

Output format.
The minimum distance.

Sample 1.
Input:
2
0 0
3 4
Output:
5.0

Sample 2.
Input:
11
4 4
-2 -2
-3 -4
-1 3
2 3
-4 0
1 1
-1 -1
3 -1
-4 2
-2 4
Output:
1.414213

Sample Input 1:
2
0 0
3 4
Sample Output 1:
5.000000000

Sample Input 2:
2
7 7
7 7
Sample Output 2:
0.000000000

*/

#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include <iomanip>

using std::vector;

struct small_x
{
    inline bool operator() (const vector<long long> &a, const vector<long long> &b)
    {
        return (a[0] < b[0]);
    }
};

struct small_y
{
    inline bool operator() (const vector<long long> &a, const vector<long long> &b)
    {
        return (a[1] < b[1]);
    }
};

long long distance (vector<long long> &a, vector<long long> &b) {
    long long x2 = std::pow(a[0] - b[0], 2);
    long long y2 = std::pow(a[1] - b[1], 2);
    return x2 + y2;
}

long long getMinDistanceNaive (vector<vector<long long>> coords) {
    long long minDist = 10e9;

    for (int i = 0; i < coords.size(); ++i) {
        for (int j = i + 1; j < coords.size(); ++j) {
            long long d = distance(coords[i], coords[j]);
            minDist = minDist > d ? d : minDist;
        }
    }

    return minDist;
}

long long getMinDistance (vector<vector<long long>> coords) {
    if (coords.size() < 5) {
        return getMinDistanceNaive(coords);
    }

    std::sort(coords.begin(), coords.end(), small_x());
    int mid_id = coords.size() / 2;
    long long mid_x = coords[mid_id][0];

    long long left_dist = getMinDistance(vector<vector<long long>>(coords.begin(), coords.begin() + mid_id));
    long long right_dist = getMinDistance(vector<vector<long long>>(coords.begin() + mid_id, coords.end()));

    long long min_dist = std::min(left_dist, right_dist);

    vector<vector<long long>>strip;
    for (int i = 0; i < coords.size(); ++i) {
        long long d = std::pow((coords[i][0] - mid_x), 2);
        if (d < min_dist) {
            strip.push_back(coords[i]);
        }
    }
    std::sort(strip.begin(), strip.end(), small_y());

    for (int i = 0; i < strip.size(); ++i) {
        int jSize = std::min(i + 8, (int) strip.size());
        for (int j = i+1; j < jSize; ++j) {
            long long d = distance(strip[i], strip[j]);
            min_dist = std::min(min_dist, d);
        }
    }

    return min_dist;
}


int main () {
    int n;
    std::cin >> n;

    vector<vector<long long>> coords;

    for (int i = 0; i < n; ++i) {
        long long x;
        long long y;
        std::cin >> x >> y;

        coords.push_back({x, y});
    }

    long long d = getMinDistance(coords);

    std::cout << std::fixed;
    std::cout << std::setprecision(6);
    std::cout << std::sqrt(d) << "\n";

    return 0;
}
