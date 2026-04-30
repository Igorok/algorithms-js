package main

import (
	"fmt"
)

func hasValidPath(grid [][]int) bool {
	shiftsByType := [][][]int{
		{{0, -1}, {0, 1}},
		{{-1, 0}, {1, 0}},
		{{0, -1}, {1, 0}},
		{{0, 1}, {1, 0}},
		{{0, -1}, {-1, 0}},
		{{0, 1}, {-1, 0}},
	}

	N := len(grid)
	M := len(grid[0])
	L := N * M

	parents := make([]int, L)
	counts := make([]int, L)

	for i := range L {
		parents[i] = -1
	}

	var getId = func(row, col int) int {
		return row*M + col
	}

	var getParent func(id int) int
	getParent = func(id int) int {
		if parents[id] == -1 {
			parents[id] = id
			counts[id] = 1
			return id
		}

		if parents[id] == id {
			return id
		}

		parent := getParent(parents[id])
		parents[id] = parent
		return parent
	}

	var unite func(id1, id2 int)
	unite = func(id1, id2 int) {
		parent1 := getParent(id1)
		count1 := counts[parent1]
		parent2 := getParent(id2)
		count2 := counts[parent2]

		if parent1 == parent2 {
			return
		}

		if count1 >= count2 {
			parents[parent2] = parent1
			counts[parent1] = count1 + count2
		} else {
			parents[parent1] = parent2
			counts[parent2] = count1 + count2
		}
	}

	for row := range N {
		for col := range M {
			val := grid[row][col] - 1
			id1 := getId(row, col)

			for _, shift := range shiftsByType[val] {
				newRow := row + shift[0]
				newCol := col + shift[1]

				if newRow == -1 || newRow == N || newCol == -1 || newCol == M {
					continue
				}

				newVal := grid[newRow][newCol] - 1
				for _, newShift := range shiftsByType[newVal] {
					oldRow := newRow + newShift[0]
					oldCol := newCol + newShift[1]

					if oldRow == row && oldCol == col {
						id2 := getId(newRow, newCol)

						unite(id1, id2)
						break
					}
				}

			}
		}
	}

	parent1 := getParent(getId(0, 0))
	parent2 := getParent(getId(N-1, M-1))

	return parent1 == parent2
}

func main() {
	fmt.Println("hasValidPath...")
	// call your solution here
}
