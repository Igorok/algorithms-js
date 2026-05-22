package main

import (
	"fmt"
)

func firstStableIndex(nums []int, k int) int {
	N := len(nums)
	inf := int(7 + 1e9)

	minVal := inf
	minRight := make([]int, N)
	for i := N - 1; i > -1; i-- {
		minVal = min(minVal, nums[i])
		minRight[i] = minVal
	}

	maxVal := -1
	for i := range N {
		maxVal = max(maxVal, nums[i])
		instable := maxVal - minRight[i]
		if instable <= k {
			return i
		}
	}

	return -1
}

func main() {
	fmt.Println("firstStableIndex...")
	// call your solution here

}
