package main

import (
	"fmt"
)

func minMoves(nums []int, limit int) int {
	N := len(nums)
	acc := make([]int, 2+limit*2)

	for i := range N / 2 {
		a, b := nums[i], nums[N-1-i]
		if a > b {
			a, b = b, a
		}
		// 1 change interval
		acc[a+1] -= 1
		// 0 change
		acc[a+b] -= 1
		acc[a+b+1] += 1
		// end of 1 change interval
		acc[b+limit+1] += 1
	}

	res := N
	curr := N

	for i := range 1 + limit*2 {
		curr += acc[i]
		res = min(res, curr)
	}

	return res
}

func main() {
	fmt.Println("minMoves...")
	// call your solution here

}
