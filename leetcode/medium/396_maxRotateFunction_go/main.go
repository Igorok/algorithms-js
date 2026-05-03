package main

import (
	"fmt"
)

func maxRotateFunction(nums []int) int {
	N := len(nums)
	sumOfNums := 0
	sumOfRot := 0

	for i, num := range nums {
		sumOfNums += num
		sumOfRot += i*num
	}

	res := sumOfRot
	for i:= 1; i < N; i++ {
		sumOfRot = sumOfRot + sumOfNums - N * nums[N-i]
		res = max(res, sumOfRot)
	}
	
	return res
}

/*
[4,3,2,6]

[4,3,2,6]
[6,4,3,2]
[2,6,4,3]
[3,2,6,4]
[4,3,2,6]


 */

func main() {
	fmt.Println("maxRotateFunction...")
	// call your solution here
}
