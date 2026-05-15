package main

import (
	"fmt"
)

func findMin(nums []int) int {
	N := len(nums)
	if N == 1 {
		return nums[0]
	}

	if nums[0] < nums[N-1] {
		return nums[0]
	}

	start := 0
	end := N - 1

	for start <= end {
		middle := (start + end) / 2

		if nums[middle] < nums[(N+middle-1)%N] && nums[middle] < nums[(middle+1)%N] {
			return nums[middle]
		}

		if nums[middle] > nums[N-1] {
			start = middle + 1
			continue
		}

		if nums[middle] < nums[N-1] {
			end = middle - 1
			continue
		}

	}

	return 0
}

func main() {
	fmt.Println("findMin...")
	// call your solution here

}
