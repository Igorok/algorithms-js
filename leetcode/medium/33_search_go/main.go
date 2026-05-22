package main

import (
	"fmt"
)

func search(nums []int, target int) int {
	N := len(nums)
	start := 0
	end := N - 1

	for start <= end {
		middle := (start + end) / 2

		if nums[middle] == target {
			return middle
		}

		if nums[0] < nums[N-1] {
			if nums[middle] < target {
				start = middle + 1
			} else {
				end = middle - 1
			}
			continue
		}

		// left side
		if target > nums[N-1] {
			if nums[middle] < nums[N-1] {
				end = middle - 1
				continue
			}
			if nums[middle] > target {
				end = middle - 1
				continue
			}
			start = middle + 1
		} else {
			// right side
			if nums[middle] > nums[N-1] {
				start = middle + 1
				continue
			}
			if nums[middle] < target {
				start = middle + 1
				continue
			}
			end = middle - 1
		}
	}

	return -1
}

func main() {
	fmt.Println("search...")
	// call your solution here

}
