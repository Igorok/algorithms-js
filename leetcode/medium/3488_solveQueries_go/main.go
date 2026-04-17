package main

import (
	"fmt"
	"math"
)

func getId(ids []int, id int) int {
	start := 0
	end := len(ids) - 1

	for start <= end {
		middle := int((start + end) / 2)
		if ids[middle] == id {
			return middle
		} else if ids[middle] > id {
			end = middle - 1
		} else {
			start = middle + 1
		}
	}

	return -1
}

func solveQueries(nums []int, queries []int) []int {
	numsByVal := make(map[int][]int)

	for id, num := range nums {
		arr, ok := numsByVal[num]
		if !ok {
			numsByVal[num] = []int{id}
		} else {
			numsByVal[num] = append(arr, id)
		}
	}

	N := len(nums)
	res := make([]int, len(queries))

	for i, id := range queries {
		arr, ok := numsByVal[nums[id]]
		if !ok || len(arr) == 1 {
			res[i] = -1
			continue
		}

		arrId := getId(arr, id)

		leftId := int(
			math.Mod(
				float64(arrId-1+len(arr)),
				float64(
					len(arr),
				),
			),
		)
		left := id - arr[leftId]
		if arr[leftId] > id {
			left = id + N - arr[leftId]
		}

		rightId := int(
			math.Mod(
				float64(arrId+1),
				float64(
					len(arr),
				),
			),
		)
		right := arr[rightId] - id
		if arr[rightId] < id {
			right = N - id + arr[rightId]
		}

		res[i] = int(min(left, right))
	}

	return res
}

func main() {
	fmt.Println("solveQueries...")
	// call your solution here
}
