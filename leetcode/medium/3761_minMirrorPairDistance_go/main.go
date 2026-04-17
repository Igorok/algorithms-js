package main

import (
	"fmt"
	"math"
)

func minMirrorPairDistance(nums []int) int {
	res := 1e9
	reversedByNum := make(map[int]int)

	reverse := func(num int) int {
		res := float64(0)
		for num > 0 {
			r := math.Mod(float64(num), float64(10))
			res = res*10 + r
			num = int(num / 10)
		}
		return int(res)
	}

	for id, num := range nums {
		prevId, ok := reversedByNum[num]
		if ok {
			dist := float64(id - prevId)
			res = min(res, dist)
		}

		reversed := reverse(num)
		reversedByNum[reversed] = id
	}

	if res == 1e9 {
		return -1
	}
	return int(res)
}

func main() {
	fmt.Println("solveQueries...")
	// call your solution here
}
