package main

import (
	"fmt"
)

func countDigitOccurrences(nums []int, digit int) int {
	res := 0

	for _, num := range nums {
		for num > 0 {
			r := num % 10
			num = num / 10
			if r == digit {
				res += 1
			}
		}
	}

	return res
}

func main() {
	fmt.Println("countDigitOccurrences...")
	// call your solution here
}
