package main

import (
	"fmt"
)

func maxValue(nums []int) []int {
	N := len(nums)
	res := make([]int, N)

	// left jump
	prev := -1
	for i, num := range nums {
		prev = max(prev, num)
		res[i] = prev
	}

	//
	acc := [2]int{nums[N-1], res[N-1]}
	for i := N - 1; i > -1; i-- {
		if res[i] > acc[0] || res[i] == acc[1] {
			res[i] = max(acc[1], res[i])
			acc[0] = min(nums[i], acc[0])
		}

		if res[i] <= acc[0] {
			acc[0] = min(acc[0], nums[i])
			acc[1] = res[i]
		}
	}

	return res
}

func main() {
	fmt.Println("maxValue...")
	// call your solution here

}
