package main

import (
	"fmt"
	"slices"
)

func minOperations(grid [][]int, x int) int {
	N := len(grid)
	M := len(grid[0])
	L := N * M
	arr := make([]int, L)

	for row := range N {
		for col := range M {
			id := row*M + col
			arr[id] = grid[row][col]
		}
	}

	slices.Sort(arr)
	// fmt.Println(arr)

	median := arr[L/2]

	res := 0

	for i := range L {
		diff := arr[i] - median
		if diff < 0 {
			diff = -diff
		}
		if diff%x != 0 {
			return -1
		}
		res += diff / x
	}

	return res
}

/*

1 2 3 4
3
4 2 3 4

2
3 4 3 4
5 6 5 6
7 8 7 8
9 10 9 10





*/

func main() {
	fmt.Println("minOperations...")
	// call your solution here
}
