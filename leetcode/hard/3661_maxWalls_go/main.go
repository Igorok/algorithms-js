package main

import (
	"fmt"
	"sort"
)


func maxWallsDestroyed(robots []int, walls []int, distance int) int {
	// 1. Sort everything to enable binary search and linear DP
	sort.Ints(robots)
	sort.Ints(walls)

	n := len(robots)
	// memo stores results for (current robot index)
	memo := make([]int, n)
	for i := range memo {
		memo[i] = -1
	}

	// Helper function to count walls in range [low, high]
	countWalls := func(low, high int) int {
		if low > high {
			return 0
		}
		// Find first wall >= low
		idx1 := sort.Search(len(walls), func(i int) bool {
			return walls[i] >= low
		})
		// Find first wall > high
		idx2 := sort.Search(len(walls), func(i int) bool {
			return walls[i] > high
		})
		return idx2 - idx1
	}

	var solve func(idx int) int
	solve = func(idx int) int {
		// Base case: no more robots left
		if idx == n {
			return 0
		}
		if memo[idx] != -1 {
			return memo[idx]
		}

		// Option 1: Fire Left
		// Range is limited by the previous robot or the max distance
		leftLimit := robots[idx] - distance
		if idx > 0 && leftLimit < robots[idx-1] {
			leftLimit = robots[idx-1]
		}
		resLeft := countWalls(leftLimit, robots[idx]-1) + solve(idx+1)

		// Option 2: Fire Right
		// Range is limited by the next robot or the max distance
		rightLimit := robots[idx] + distance
		if idx < n-1 && rightLimit > robots[idx+1] {
			rightLimit = robots[idx+1]
		}
		resRight := countWalls(robots[idx]+1, rightLimit) + solve(idx+1)

		// Store and return the better choice
		memo[idx] = int(math.Max(float64(resLeft), float64(resRight)))
		return memo[idx]
	}

	return solve(0)
}


func maxWalls_1(robots []int, distance []int, walls []int) int {
	return 0
}


func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
