package main

import (
	"fmt"
	"math"
)

func maximumJumps(nums []int, target int) int {
	_target := float64(target)
	N := len(nums)
	acc := make([]int, N)
	for i := 1; i < N; i++ {
		acc[i] = -1
	}

	for i := range N {
		if acc[i] == -1 {
			continue
		}
		for j := i + 1; j < N; j++ {
			diff := math.Abs(float64(nums[i] - nums[j]))
			if diff <= _target {
				acc[j] = max(acc[j], acc[i]+1)
			}
		}
	}

	// fmt.Println(
	// 	"nums", nums,
	// 	"acc", acc,
	// )

	return acc[N-1]
}

func main() {
	fmt.Println("maximumJumps...")
	// call your solution here

}
