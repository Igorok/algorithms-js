package main

import (
	"fmt"
	"slices"
)

func minimumCost(cost []int) int {
	slices.Sort(cost)
	n := len(cost)
	i := n - 1
	res := 0

	for i > -1 {
		for range 2 {
			res += cost[i]
			i -= 1
			if i < 0 {
				break
			}
		}
		if i > -1 {
			i -= 1
		}
	}

	return res

}
func main() {
	fmt.Println("minimumCost...")
	// call your solution here

}
