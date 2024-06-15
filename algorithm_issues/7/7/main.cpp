/*

Given a set of points and a set of segments on a line, compute, for each point, the number of segments it is contained in.
Input: A list of segments and a list of points.
Output: The number of segments containing each point.

Sample 1.
Input:
2 3
0 5
7 10
1 6 11
Output:
1 0 0

Sample 2.
Input:
1 3
-10 10
-100 100 0
Output:
0 0 1

Sample 3.
Input:
3 2
0 5
-3 2
7 10
1 6
Output:
2 0

// trick

i:
4 5
1 5
5 10
6 10
7 12
4 5 10 11 13
o:
1 2 2 1 0

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using std::vector;
using std::map;

struct Point {
    long long coord;
    char type;

    Point (long long c, char t): coord(c), type(t)
    {}
};

map<char, int> typeWeight {
    {'s', -1},
    {'p', 0},
    {'e', 1},
};

struct small_coord
{
    inline bool operator() (const Point &a, const Point &b)
    {
        if (a.coord != b.coord) {
            return a.coord < b.coord;
        }

        return a.coord + typeWeight[a.type] < b.coord + typeWeight[b.type];
    }
};



void print_points_segments (vector<Point> &allPoints, vector<long long> &points) {
    std::sort(allPoints.begin(), allPoints.end(), small_coord());

    long long segments = 0;
    map<long long, long long> segmentsByPoints;

    for (int i = 0; i < allPoints.size(); ++i) {
//        std::cout << allPoints[i].coord << " " << allPoints[i].type << "\n";


        if (allPoints[i].type == 's') {
            segments += 1;
        } else if (allPoints[i].type == 'e') {
            segments -= 1;
        } else {
            segmentsByPoints[allPoints[i].coord] = segments;
        }
    }

    for (int i = 0; i < points.size(); ++i) {
        std::cout << segmentsByPoints[points[i]] << " ";
    }

    std::cout << "\n";
}

int main() {
    int n, m;
    std::cin >> n >> m;

    vector<Point> allPoints;
    vector<long long> points;

    for (int i = 0; i < n; ++i) {
        long long start;
        long long end;

        std::cin >> start >> end;

        allPoints.push_back(Point(start, 's'));
        allPoints.push_back(Point(end, 'e'));
    }

    for (int i = 0; i < m; ++i) {
        long long point;
        std::cin >> point;

        allPoints.push_back(Point(point, 'p'));

        points.push_back(point);
    }

    print_points_segments(allPoints, points);
}
