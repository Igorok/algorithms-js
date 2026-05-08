package main

import (
	"fmt"
)

func rotateTheBox(boxGrid [][]byte) [][]byte {
	N := len(boxGrid)
	M := len(boxGrid[0])

	res := make([][]byte, M)
	for c := range M {
		res[c] = make([]byte, N)
	}

	fillResColl := func(row, col, count int) {
		if count == 0 {
			return
		}

		for count > 0 {
			res[row][col] = '#'
			row -= 1
			count -= 1
		}
	}

	for row := range N {
		count := 0
		for col := range M {
			res[col][N-row-1] = '.'

			if boxGrid[row][col] == '#' {
				count += 1
			}
			if boxGrid[row][col] == '*' {
				res[col][N-row-1] = '*'
				fillResColl(col-1, N-row-1, count)
				count = 0
			}
			if col == M-1 {
				fillResColl(col, N-row-1, count)
				count = 0
			}
		}
	}

	return res
}

func main() {
	fmt.Println("rotateTheBox...")
	// call your solution here
}
