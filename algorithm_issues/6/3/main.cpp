#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using std::vector;

struct Product {
    int cost;
    int weight;
    double price_per_kilo;

    Product(int c, int w) : cost(c), weight(w)
    {
        price_per_kilo = (double)cost / (double)weight;
    }
};

struct great_price
{
    inline bool operator() (const Product& a, const Product& b)
    {
        return (a.price_per_kilo > b.price_per_kilo);
    }
};

double get_optimal_value(int capacity, vector<Product> &goods) {
    double value = 0.0;

    std::sort(goods.begin(), goods.end(), great_price());

    for (int i = 0; i < goods.size(); ++i) {
        if (capacity == 0) {
            return value;
        }

        int takenValue = std::min(capacity, goods[i].weight);
        value += goods[i].price_per_kilo * (double)takenValue;
        capacity -= takenValue;
    }

    return value;
}

int main() {
    int n;
    int capacity;

    std::cin >> n >> capacity;

    vector<Product> goods;
    for (int i = 0; i < n; ++i) {
        int cost;
        int weight;

        std::cin >> cost >> weight;
        Product p(cost, weight);

        goods.push_back(p);
    }

    double value = get_optimal_value(capacity, goods);

    std::cout << std::fixed;
    std::cout << std::setprecision(4);
    std::cout << value << "\n";

    return 0;
}
