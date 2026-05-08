package main

import (
	"fmt"
)

func rotate(matrix [][]int) {
	N := len(matrix)

	for start := range N / 2 {
		end := N - start - 1

		for iteration := range end - start {
			currV := matrix[start][start+iteration]

			nextV := matrix[start+iteration][end]
			matrix[start+iteration][end] = currV
			currV = nextV

			nextV = matrix[end][end-iteration]
			matrix[end][end-iteration] = currV
			currV = nextV

			nextV = matrix[end-iteration][start]
			matrix[end-iteration][start] = currV
			currV = nextV

			matrix[start][start+iteration] = currV
		}

	}

}

func main() {
	fmt.Println("rotate...")
	// call your solution here
}

/*
[0,0]->[0,2]
[0,2]->[2,2]
[2,2]->[2,0]
[2,0]->[0,0]

[0,1]->[1,2]
[1,2]->[2,1]
[2,1]->[1,1]
[1,1]->[0,1]


*/
