package main

import (
	"fmt"
)

func maxJumps(arr []int, d int) int {
	N := len(arr)
	memo := make([]int, N)

	var rec func (id int) int
	rec = func (id int) int {
		if memo[id] != 0 {
			return memo[id]
		}
		res := 1
		
		for i := id+1; i < min(N, id+d+1); i++ {
			if arr[i] >= arr[id] {
				break
			}
			r := rec(i)
			res = max(res, r+1)
		}
		for i := id-1; i > max(-1, id-d-1); i-- {
			if arr[i] >= arr[id] {
				break
			}
			r := rec(i)
			res = max(res, r+1)
		}

		memo[id] = res
		
		return res
	}

	res := 1
	for i := range N {
		r := rec(i)
		res = max(res, r)
	}
	
	return res
}

func main() {
	fmt.Println("maxJumps...")
}
