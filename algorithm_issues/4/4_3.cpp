#include <iostream>
#include <cstdlib>
#include <vector>

using std::vector;

long long getMaxMultiply(int length, vector<int> nums) {
    long long maxMul = 0;
    for (int i = 0; i < length; ++i) {
        for (int j = i+1; j < length; ++j) {
            long long m = (long long) nums[i] * nums[j];
            if (m > maxMul) {
                maxMul = m;
            }
        }
    }

    return maxMul;
}

long long getMaxMultiply2(int length, vector<int> nums) {
    vector<int> a(2, -1);
    vector<int> b(2, -1);

    for (int i = 0; i < length; ++i) {
        if (nums[i] > a[0]) {
            a[0] = nums[i];
            a[1] = i;
        }
    }

    for (int i = 0; i < length; ++i) {
        if (nums[i] > b[0] && i != a[1]) {
            b[0] = nums[i];
            b[1] = i;
        }
    }

    return (long long) a[0] * b[0];
}

void test () {
    for (int i = 0; i < 100; ++i) {
        // length >= 2
        int length = std::rand() % 5 + 2;
        vector<int> numbers;
        for (int j = 0; j < length; ++j) {
            int value = std::rand() % 10 + 1;
            numbers.push_back(value);
            std::cout << value << " ";
        }
        std::cout << "\n";

        long long r1= getMaxMultiply(length, numbers);
        long long r2= getMaxMultiply2(length, numbers);

        if (r1 == r2) {
            std::cout << "OK" << "\n";
        } else {
            std::cout << "ERROR " << r1 << " != " << r2 << "\n";
            break;
        }
    }
}

int main() {

    test();

    int l = 0;
    vector<int> nums;
    std::cin >> l;

    for (int i = 0; i < l; ++i) {
        int v;
        std::cin >> v;
        nums.push_back(v);
    }

    std::cout << getMaxMultiply2(l, nums) << std::endl;

    return 0;
}