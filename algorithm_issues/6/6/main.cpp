/*

Input:
3
1 3
2 5
3 6
Output:
1
3

---

Input:
4
4 7
1 3
2 5
5 6
Output:
2
3 6

---

Input:
5
4 7
1 3
2 5
5 6
1 8
Output:
2
3 6

---

There are several intervals of time. We need to find a minimum count of points of time to cover all intervals.
We will sort intervals by the end. We take the end of first interval and we know - other intervals doesn't finished yet.
So we will get all intervals where start is less thet current number;
*/

#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

struct Interval {
	long long start;
	long long end;
	bool used;

	Interval (long long s, long long e) : start(s), end(e) {
		used = false;
	}
};

struct min_end
{
    inline bool operator() (const Interval& a, Interval& b)
    {
        return a.end < b.end;
    }
};

vector<long long> get_points (int n, vector< Interval > intervals) {
	vector<long long> points;
	std::sort(intervals.begin(), intervals.end(), min_end());

	for (int i = 0; i < n; ++i) {
		Interval& interval = intervals[i];
		// std::cout << "start " << interval.start << " end " << interval.end << "\n";

		if (interval.used) {
			continue;
		}

		points.push_back(interval.end);
		interval.used = true;

		for (int j = i + 1; j < n; ++j) {
			Interval& current = intervals[j];
			if (current.used) {
				continue;
			}
			if (current.start <= interval.end) {
				current.used = true;
			}
		}
	}

	return points;
}

int main () {
	int n;
	vector< Interval > intervals;

	std::cin >> n;
	for (int i = 0; i < n; ++i) {
		long long start;
		long long end;
		std::cin >> start >> end;
		intervals.push_back(Interval(start, end));
	}

	vector<long long> points = get_points(n, intervals);
	std::cout << points.size() << "\n";

	for (int i = 0; i < points.size(); ++i) {
		std::cout << points[i] << " ";
	}
	std::cout << "\n";

	return 0;
}