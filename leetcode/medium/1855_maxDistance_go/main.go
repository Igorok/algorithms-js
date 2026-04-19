package main

import (
	"fmt"
)

func getId(nums *[]int, num int) int {
	start := 0
	end := len(*nums) - 1
	res := -1

	for start <= end {
		middle := int((start + end) / 2)

		if (*nums)[middle] >= num {
			res = middle
			start = middle + 1
		} else {
			end = middle - 1
		}
	}

	return res
}

func maxDistance(nums1 []int, nums2 []int) int {
	res := 0

	for id1, num := range nums1 {
		id2 := getId(&nums2, num)
		if id2 >= id1 {
			res = max(res, id2-id1)
		}
	}
	return res
}

func main() {
	fmt.Println("maxDistance...")
	// call your solution here
}
