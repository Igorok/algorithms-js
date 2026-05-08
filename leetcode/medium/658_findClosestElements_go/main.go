package main

import (
	"fmt"
	"math"
)

func findClosestElements(arr []int, k int, x int) []int {
	res := make([]int, 0, k)
	for _, num := range arr {
		if len(res) < k {
			res = append(res, num)
			continue
		}

		prevDiff := math.Abs(float64(x) - float64(res[0]))
		currDiff := math.Abs(float64(x) - float64(num))

		if prevDiff > currDiff {
			res = res[1:]
			res = append(res, num)
		}
	}

	return res
}

func main() {
	fmt.Println("findClosestElements...")
	// call your solution here
}
