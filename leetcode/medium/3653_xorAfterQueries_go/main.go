package main

import (
	"fmt"
	"math"
)

/*


golang invalid operation: operator % not defined on variable of type float64


*/

func xorAfterQueries(nums []int, queries [][]int) int {
	MOD := float64(1e9 + 7)

	for _, arr := range queries {
		idx := arr[0]
		for idx <= arr[1] {
			res := math.Mod(float64(nums[idx] * arr[3]), MOD)
			nums[idx] = int(res)
			idx += arr[2]
		}
	}

	res := 0
	for _, val := range nums {
		res ^= val
	}

	return res
}

func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
