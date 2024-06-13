/*

Sample Input 1:
5
2 3 9 2 9
Sample Output 1:
2

Sample Input 2:
4
1 2 3 4
Sample Output 2:
0

*/


#include <iostream>
#include <vector>

using std::vector;

/*
long long get_number_of_inversions(vector<int> &a, vector<int> &b, size_t left, size_t right) {
  long long number_of_inversions = 0;
  if (right <= left + 1) return number_of_inversions;
  size_t ave = left + (right - left) / 2;
  number_of_inversions += get_number_of_inversions(a, b, left, ave);
  number_of_inversions += get_number_of_inversions(a, b, ave, right);
  //write your code here
  return number_of_inversions;
}
*/


/*

12
1 2 3 1 2 3 1 2 3 3 2 1

3 + 6 + 2 + 4 + 1 + 2 + 2 + 1 = 21

                1 2 3 1 2 3      1 2 3 3 2 1
        1 2 3       1 2 3      1 2 3        3 2 1
1 2     3       1 2     3      1 2      3        3 2    1

1+2
0   0   0   0   0   0   1   0
0   0   0   2
1


*/
long long num_of_inv = 0;

vector<long long> merge_sort(vector<long long> &a) {
    if (a.size() < 2) {
        return a;
    }

    vector<long long> sorted;

    int m = a.size() / 2;
    vector<long long> left = vector<long long>(a.begin(), a.begin() + m);
    vector<long long> right = vector<long long>(a.begin() + m, a.end());

    left = merge_sort(left);
    right = merge_sort(right);

    int i = 0;
    int j = 0;

    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            sorted.push_back(left[i]);
            ++i;
        } else {
            long long d = left.size() - i;
            num_of_inv += d;

            sorted.push_back(right[j]);
            ++j;
        }
    }

    while (i < left.size()) {
        sorted.push_back(left[i]);
        ++i;
    }

    while (j < right.size()) {
        sorted.push_back(right[j]);
        ++j;
    }

    return sorted;
}

int main() {
    int n;
    std::cin >> n;
    vector<long long> a(n);

    for (size_t i = 0; i < a.size(); i++) {
        std::cin >> a[i];
    }

    vector<long long>sorted = merge_sort(a);

    for (int i = 0; i < sorted.size(); ++i) {
        std::cout << sorted[i] << " ";
    }
    std::cout << "\n";

    std::cout << num_of_inv << "\n";
}
