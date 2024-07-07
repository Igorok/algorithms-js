#include<iostream>

class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int sum = 0;

        while (numBottles >= numExchange) {
            int exchanged = int(numBottles / numExchange);
            int remainder = numBottles % numExchange;
            int drinked = numExchange * exchanged;

            sum += drinked;

            numBottles = exchanged + remainder;
        }

        return sum + numBottles;
    }
};

int main () {
    Solution *s = new Solution();
    std::cout << s->numWaterBottles(9, 3) << '\n';
    std::cout << s->numWaterBottles(15, 4) << '\n';

    return 0;
}