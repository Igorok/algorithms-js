package main

import (
	"fmt"
)

func canReach_0(s string, minJump int, maxJump int) bool {
	N := len(s)
	memo := make([]int, N)

	if s[N-1] == '1' {
		return false
	}

	var rec func(id int) bool
	rec = func(id int) bool {
		if memo[id] != 0 {
			return memo[id] == 1
		}

		if id == N-1 {
			return true
		}

		start := id + minJump
		if start >= N {
			memo[id] = -1
			return false
		}
		end := min(id+maxJump, N-1)

		for i := start; i <= end; i++ {
			if s[i] != '0' {
				continue
			}
			r := rec(i)
			if r {
				memo[id] = 1
				return true
			}
		}

		memo[id] = -1
		return false
	}

	return rec(0)
}

func canReach(s string, minJump int, maxJump int) bool {
	N := len(s)
	if s[N-1] == '1' || s[0] == '1' {
		return false
	}
	queue := make([]int, 0, N+1)
	queue = append(queue, 0)

	for i := range N {
		if s[i] == '1' {
			continue
		}
		for queue[0]+maxJump < i {
			queue = queue[1:]
			if len(queue) == 0 {
				return false
			}
		}
		if i < queue[0]+minJump {
			continue
		}

		queue = append(queue, i)
	}

	return queue[len(queue)-1] == N-1
}

/*

0 1 2 3 4 5 6 7
0 0 1 1 1 0 1 0

2 4
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
0 0 0 0 0 0 0 1 1 1 1  1  0  1  0  1  1  1
- - x x x
0+2,0+4 = 2,4
2+2, 4+4 = 4,8
4+2, 8+4 = 6,12
6+2,12+4 = 8,16
8+2,16+4 = 10,20


3,5
0 1 2 3 4 5 6 7
0 0 1 1 1 0 1 0


7, 10
0 1 2 3 4 5 6
0 0 0 0 0 0 0
*/

func main() {
	fmt.Println("canReach...")
	// call your solution here

}
