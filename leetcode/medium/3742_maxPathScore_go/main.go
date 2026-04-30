package main

import (
	"fmt"
	"slices"
)

func maxPathScore(grid [][]int, k int) int {
	N := len(grid)
	M := len(grid[0])

	prev := make([][]int, M)
	curr := make([][]int, M)

	for row := range N {
		curr = make([][]int, M)

		for col := range M {
			curr[col] = make([]int, k+1)
			for i := range k + 1 {
				curr[col][i] = -1
			}

			if row == 0 && col == 0 {
				curr[col][0] = 0
				continue
			}

			score := grid[row][col]
			cost := 0
			if score > 0 {
				cost = 1
			}

			if row > 0 {
				for c := range k + 1 {
					if prev[col][c] == -1 || c+cost > k {
						continue
					}
					curr[col][c+cost] = max(curr[col][c+cost], prev[col][c]+score)
				}
			}

			if col > 0 {
				for c := range k + 1 {
					if curr[col-1][c] == -1 || c+cost > k {
						continue
					}
					curr[col][c+cost] = max(curr[col][c+cost], curr[col-1][c]+score)
				}
			}
		}

		prev = curr
		curr = nil
	}

	res := slices.Max(prev[M-1])

	return res
}

func main() {
	fmt.Println("maxPathScore...")
	// call your solution here
}
