package main

import (
	"fmt"
	"slices"
)

func minIncrementForUnique(nums []int) int {
	N := len(nums)
	slices.Sort(nums)
	res := 0

	for i := 1; i < N; i++ {
		if nums[i-1] >= nums[i] {
			diff := nums[i-1] - nums[i] + 1
			res += diff
			nums[i] += diff
		}
	}
	
	return res
}

func main() {
	fmt.Println("minIncrementForUnique...")
}
