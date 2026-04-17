package main

import (
	"fmt"
	"math"
)

func minimumAverageDifference(nums []int) int {
	N := len(nums)
	prefixSum := make([]int, N)
	for i, n := range nums {
		prev := 0
		if i > 0 {
			prev = prefixSum[i-1]
		}
		prefixSum[i] = n + prev
	}

	res := 0
	diff := int(1e9)

	for i, _ := range prefixSum {
		leftCnt := i+1
		leftAvg := int(math.Floor(float64(prefixSum[i]) / float64(leftCnt)))
		rightCnt := N - i - 1
		rightAvg := 0
		if rightCnt > 0 {
			rightAvg = int(math.Floor(float64(prefixSum[N-1]-prefixSum[i]) / float64(rightCnt)))
		}

		r := int(math.Abs(float64(leftAvg) - float64(rightAvg)))
		if r < diff {
			diff = r
			res = i
		}
	}

	return res
}

func main() {
	fmt.Println("minimumDistance...")
	// call your solution here
}
