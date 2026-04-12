package main

import (
	"fmt"
	"math"
)

func minimumDistance(nums []int) int {
	idsByNum := make(map[int][]int)
	res := -1

	getDiff := func(arr []int, id1 int, id2 int) int {
		return int(math.Abs(float64(arr[id1]) - float64(arr[id2])))
	}

	for id, num := range nums {
		arr, ok := idsByNum[num]
		if !ok {
			idsByNum[num] = []int{id}
			continue
		}
		idsByNum[num] = append(arr, id)
		if len(idsByNum[num]) < 3 {
			continue
		}

		last := len(idsByNum[num]) - 1
		r := getDiff(idsByNum[num], last, last-1) + getDiff(idsByNum[num], last, last-2) + getDiff(idsByNum[num], last-1, last-2)

		if res == -1 {
			res = r
		} else {
			res = min(res, r)
		}
	}

	return res
}

func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
