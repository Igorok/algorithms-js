#include<iostream>
#include<vector>

using std::vector;

int main()
{
    int n;
    int m;

    std::cin >> n >> m;

    vector<vector<int>> field;

    for (int i = 0; i < n; ++i) {
        vector<int> row;
       for (int j = 0; j < m; ++j) {
           int val;
           std::cin >> val;
            row.push_back(val);
        }
        field.push_back(row);
    }

    vector<vector<int>> memo;
    for (int i = 0; i < n; ++i) {
        vector<int> row;
       for (int j = 0; j < m; ++j) {
            row.push_back(10e6);
        }
        memo.push_back(row);
    }

    memo[0][0] = field[0][0];

    for (int i = 0; i < n; ++i) {
       for (int j = 0; j < m; ++j) {
            if (i > 0 && j > 0) {
                int min = std::min(
                    memo[i-1][j],
                    memo[i][j-1]
                ) + field[i][j];
                memo[i][j] = std::min(min, memo[i][j]);
            }

            if (j > 0 && i == 0) {
                memo[i][j] = std::min(
                    memo[i][j],
                    memo[i][j-1] + field[i][j]
                );
            }

            if (i > 0 && j == 0) {
                memo[i][j] = std::min(
                    memo[i][j],
                    memo[i-1][j] + field[i][j]
                );
            }
        }
    }

    std::cout << memo[n-1][m-1] << "\n";

    return 0;
}
