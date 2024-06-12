
/*

Input format.
The first line of the input contains an integer n.
The next line contains a sequence of n integers  a[0], a[1], ..., a[n−1].

Output format.
Output this sequence sorted in non-decreasing order.

Input:
5
2 3 9 2 2
Output:
2 2 2 3 9


*/

#include<iostream>
#include<vector>
#include <cstdlib>

using std::vector;

vector<long long> get_sorted (vector<long long> &listN) {
    int size = listN.size();

    if (size < 2) {
        return listN;
    }

    int idx = std::rand() % size;

    vector<long long> left;
    vector<long long> middle;
    vector<long long> right;

    for (int i = 0; i < size; ++i) {
        if (listN[i] == listN[idx]) {
            middle.push_back(listN[i]);
            continue;
        }
        if (listN[i] < listN[idx]) {
            left.push_back(listN[i]);
            continue;
        }
        if (listN[i] > listN[idx]) {
            right.push_back(listN[i]);
            continue;
        }
    }

    left = get_sorted(left);
    right = get_sorted(right);

    for (int i = 0; i < middle.size(); ++i) {
        left.push_back(middle[i]);
    }

    for (int i = 0; i < right.size(); ++i) {
        left.push_back(right[i]);
    }

    return left;
}

int main () {
    int n;
    vector<long long> listN;

    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        long long v;
        std::cin >> v;
        listN.push_back(v);
    }

    vector<long long> sorted = get_sorted(listN);

    for (int i = 0; i < n; ++i) {
        std::cout << sorted[i] << " ";
    }
    std::cout << "\n";

    return 0;
}
