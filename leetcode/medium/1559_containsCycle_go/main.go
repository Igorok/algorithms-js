package main

import (
	"fmt"
)


func containsCycle(grid [][]byte) bool {
	shifts := [][]int{{1,0}, {-1,0}, {0,1},{0,-1}}
	N := len(grid)
	M := len(grid[0])
	
	memo := make([][]int, N)
	for r := range N {
		memo[r] = make([]int, M)
		for c := range M {
			memo[r][c] = -1
		}
	}
	
	var dfs func (row int, col int, prevRow int, prevCol int) int
	dfs = func (row int, col int, prevRow int, prevCol int) int {
		if memo[row][col] != -1 {
			return memo[row][col]
		}
		
		memo[row][col] = 0
		res := 0
		
		for _, shift := range shifts {
			newRow := row + shift[0]
			newCol := col + shift[1]
			
			if newRow == -1 || newCol == -1 || newRow == N || newCol == M || (newRow == prevRow && newCol == prevCol) || grid[row][col] != grid[newRow][newCol] {
				continue
			}
			
			if memo[newRow][newCol] != -1 {
				res = max(res, 1)
				continue
			}
			
			if memo[newRow][newCol] != -1 {
				continue
			}
			
			r := dfs(newRow, newCol, row, col)
			
			res = max(res, r)
		}
		
		if res == 0 {
			return 0
		}
		
		memo[row][col] = 1 + res
		
		return memo[row][col]
	}
	
	for r := range N {
		for c := range M {
			if memo[r][c] != -1 {
				continue
			}
			
			res := dfs(r, c, r, c)
			if res > 3 {
				return true
			}
		}
	}
	
	return false
}

func main() {
	fmt.Println("containsCycle...")
	// call your solution here
}
