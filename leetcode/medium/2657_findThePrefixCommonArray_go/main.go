package main

import (
	"fmt"
)

func findThePrefixCommonArray(A []int, B []int) []int {
	N := len(A)

	memo := make(map[int]int)
	res := make([]int, N)

	diff := 0

	for i := range N {
		a := A[i]
		b := B[i]

		memo[a] += 1
		if memo[a] == 2 {
			diff -= 1
		} else {
			diff += 1
		}

		memo[b] += 1
		if memo[b] == 2 {
			diff -= 1
		} else {
			diff += 1
		}

		res[i] = i + 1 - (diff / 2)
	}

	return res
}

func main() {
	fmt.Println("findThePrefixCommonArray...")
	// call your solution here

}
