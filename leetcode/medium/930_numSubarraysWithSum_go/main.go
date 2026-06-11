package main

import (
	"fmt"
)

func numSubarraysWithSum(nums []int, goal int) int {
	N := len(nums)
	sumOfNum := 0
	left := 0
	ones := make([]int, 0, 100)

	res := 0
	for right := range N {
		sumOfNum += nums[right]
		if nums[right] == 1 {
			ones = append(ones, right)
		}

		for sumOfNum > goal {
			sumOfNum -= nums[left]
			left += 1
			if len(ones) > 0 && ones[0] < left {
				ones = ones[1:]
			}
		}

		if sumOfNum == goal {
			id := right
			if len(ones) > 0 {
				id = ones[0]
			}
			diff := id - left + 1
			res += diff
		}
	}

	return res
}

/*

0,0,1,0,0
0,0,3,3,3

*/

func main() {
	fmt.Println("numSubarraysWithSum...")
	// call your solution here

}
