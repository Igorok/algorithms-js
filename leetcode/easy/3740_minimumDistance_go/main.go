package main

import (
	"fmt"
	"math"
)

func minimumDistance(nums []int) int {
	res := -1
	idsByVal := make(map[int][]int)

	getAbsDist := func(val, id1, id2 int) int {
		r := math.Abs(float64(idsByVal[val][id1]) - float64(idsByVal[val][id2]))
		return int(r)
	}

	for id, val := range nums {
		arr, ok := idsByVal[val]
		if ok {
			idsByVal[val] = append(arr, id)
			if len(idsByVal[val]) >= 3 {
				last := len(idsByVal[val]) - 1
				r := getAbsDist(val, last, last-1) + getAbsDist(val, last, last-2) + getAbsDist(val, last-1, last-2)

				if res == -1 {
					res = r
				} else {
					res = min(res, r)
				}
			}
		} else {
			idsByVal[val] = []int{id}
		}
	}

	return res
}

func main() {
	fmt.Println("minimumDistance...")
	// call your solution here
}
