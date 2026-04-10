package main

import (
	"cmp"
	"fmt"
	"slices"
)

func matrixSum(nums [][]int) int {
	sorted := [][]int{}

	for _, arr := range nums {
		slices.SortFunc(arr, func(a, b int) int {
			return cmp.Compare(b, a) // b перед a даст обратный порядок
		})
		sorted = append(sorted, arr)
	}

	res := 0

	N := len(sorted)
	M := len(sorted[0])

	for col := range(M) {
		r := -1
		for row := range(N) {
			r = max(r, sorted[row][col])
		}
		res += r
	}

	return res
}

func main() {
	fmt.Println("minimumDistance...")
	// call your solution here
}
