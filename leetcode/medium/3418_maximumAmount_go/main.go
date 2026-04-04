package main

import (
	"fmt"
)

/*

*, 			10, -1, -1
10, -3, -3, *

???
*, 			10, -1, -1
10, -3, -3, 5

???
*, 			10, -1, -1
10, -3, -3, -5
10, -3, -3, + -5 = 7, -3, -5
10, -1, -1, + -5 = 9, -1, -5

???
*, 			8, -1, -1
10, -6, -6, 5

8, -1, -1 = 13, -1, -1
10, -6, -6 = 15, -6, -6

*, 			8, -1, -1
10, -6, -6, -5
8, -1, -1 = 7, -1, -5
10, -6, -6 = 5, -6, -6

13, -1, -1
15, -6, -6
+ -5
13, -1, -1 = 12, -1, -5
15, -6, -6 = 10, -6, -6


Do you know the leetcode issue "3418. Maximum Amount of Money Robot Can Earn"?

I have a trouble here.
I see a situation:
8, -1, -1
10, -6, -6
+ 5
I will select 10, -6, -6 and I will have 15, -6, -6 instead of 13, -1, -1
But then I have a situatioin
+ -5
and 15, -6, -6 plus -5 is 15, -6, -6
but if I selected 8, -1, -1 I can reach a 12, -1, -5

And I have not ideas how to awoid it.


*/

func maximumAmount(coins [][]int) int {
	const inf int = 1e9
	// fmt.Println(coins)
	m, n := len(coins), len(coins[0])

	dp := [][][3]int{}

	for r := range m {
		row := make([][3]int, n)
		dp = append(dp, row)

		for c := range n {
			for k := range 3 {
				dp[r][c][k] = -inf
			}
		}
	}

	// fmt.Println(dp)

	for r := range m {
		for c := range n {
			if r == 0 && c == 0 {
				dp[r][c][0] = coins[r][c]
				dp[r][c][1] = max(coins[r][c], 0)
				dp[r][c][2] = max(coins[r][c], 0)
				continue
			}

			for k := range 3 {
				prev := -inf

				if r != 0 {
					prev = max(prev, dp[r-1][c][k])
				}
				if c != 0 {
					prev = max(prev, dp[r][c-1][k])
				}

				if k == 0 {
					dp[r][c][k] = prev + coins[r][c]
					continue
				}

				if coins[r][c] >= 0 {
					dp[r][c][k] = prev + coins[r][c]
					continue
				}

				prevLayer := -inf
				if r != 0 {
					prevLayer = max(prevLayer, dp[r-1][c][k-1])
				}
				if c != 0 {
					prevLayer = max(prevLayer, dp[r][c-1][k-1])
				}

				dp[r][c][k] = max(
					prev+coins[r][c],
					prevLayer,
				)

			}
		}
	}

	// fmt.Println(dp)

	return max(dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2])
}

func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
