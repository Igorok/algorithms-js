package main

import (
	"fmt"
)

func rotateGrid(grid [][]int, k int) [][]int {
	N := len(grid)
	M := len(grid[0])

	res := make([][]int, N)
	for row := range N {
		res[row] = make([]int, M)
	}

	steps := min(N, M) / 2
	for step := range steps {
		width := N - 2 * step
		height := M - 2 * step
		length := (width+height)*2 - 4

		acc := make([]int, 0, length)
		for row := step; row < N-step; row++ {
			acc = append(acc, grid[row][step])
		}
		for col := step + 1; col < M-step; col++ {
			acc = append(acc, grid[N-1-step][col])
		}
		for row := N - 2 - step; row > step-1; row-- {
			acc = append(acc, grid[row][M-1-step])
		}
		for col := M - 2 - step; col > step; col-- {
			acc = append(acc, grid[step][col])
		}

		// fmt.Println(
		// 	"length", length,
		// 	"len", len(acc),
		// )

		rot := k % length
		id := 0
		for row := step; row < N-step; row++ {
			resId := (length + id - rot) % length
			res[row][step] = acc[resId]
			id +=1
		}
		for col := step + 1; col < M-step; col++ {
			resId := (length + id - rot) % length
			res[N-1-step][col] = acc[resId]
			id +=1
		}
		for row := N - 2 - step; row > step-1; row-- {
			resId := (length + id - rot) % length
			res[row][M-1-step] = acc[resId]
			id +=1
		}
		for col := M - 2 - step; col > step; col-- {
			resId := (length + id - rot) % length
			res[step][col] = acc[resId]
			id +=1
		}

		// fmt.Println(acc)
	}

	return res
}

func main() {
	fmt.Println("rotateGrid...")
	// call your solution here
}
