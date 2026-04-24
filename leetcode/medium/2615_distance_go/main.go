package main

import (
	"fmt"
)

func distance(nums []int) []int64 {
	numsData := make(map[int][]int64)
	localArrId := make(map[int]int)

	for id, val := range nums {
		_, ok := numsData[val]
		if !ok {
			numsData[val] = make([]int64, 0, 100)
		}
		n := len(numsData[val])
		var prev int64 = 0
		if n > 0 {
			prev = numsData[val][n-1]
		}
		localArrId[id] = n
		numsData[val] = append(numsData[val], prev+int64(id))
	}

	res := make([]int64, len(nums))

	for id, val := range nums {
		n := len(numsData[val])
		if n == 1 {
			res[id] = 0
			continue
		}

		localId := localArrId[id]

		r := int64(0)

		// left sum always less than cnt*id
		if localId > 0 {
			left := numsData[val][localId-1]
			r += int64(id*localId) - left
		}

		// right sum always great that cnt*id
		if localId < n-1 {
			r += (numsData[val][n-1] - numsData[val][localId]) - int64(id)*int64(n-localId-1)
		}

		res[id] = r
	}

	return res
}

func main() {
	fmt.Println("distance...")
	// call your solution here
}
