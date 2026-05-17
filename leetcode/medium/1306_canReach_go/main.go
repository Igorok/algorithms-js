package main

import (
	"fmt"
)

func canReach(arr []int, start int) bool {
	N := len(arr)
	visited := make([]int, N)

	var dfs func(id int) int
	dfs = func(id int) int {
		if visited[id] != 0 {
			return visited[id]
		}

		if arr[id] == 0 {
			visited[id] = 1
			return visited[id]
		}

		visited[id] = -1

		if id-arr[id] > -1 {
			visited[id] = dfs(id - arr[id])
		}

		if visited[id] != 1 && id+arr[id] < N {
			visited[id] = dfs(id + arr[id])
		}

		return visited[id]
	}

	return dfs(start) == 1
}

func main() {
	fmt.Println("canReach...")
}
