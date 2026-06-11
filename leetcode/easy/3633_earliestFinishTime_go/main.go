package main

import (
	"cmp"
	"fmt"
	"slices"
)

var inf = int(1e9)

func sortByEnd(a, b []int) int {
	return cmp.Compare(a[0], b[0])
}

func getArr(StartTime []int, Duration []int) [][]int {
	n := len(StartTime)
	arr := make([][]int, n)
	for i := range n {
		arr[i] = []int{StartTime[i], Duration[i], inf, inf}
	}
	slices.SortFunc(arr, sortByEnd)

	// min duration
	acc := inf
	for i := range n {
		acc = min(acc, arr[i][1])
		arr[i][2] = acc
	}
	// min final
	acc = inf
	for i := n - 1; i > -1; i-- {
		acc = min(acc, arr[i][0]+arr[i][1])
		arr[i][3] = acc
	}
	return arr
}

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	n := len(landStartTime)
	m := len(waterStartTime)

	landArr := getArr(landStartTime, landDuration)
	waterArr := getArr(waterStartTime, waterDuration)

	// fmt.Println("landArr", landArr)
	// fmt.Println("waterArr", waterArr)

	var getMinEnd = func(arr [][]int, start int) int {
		left := 0
		right := len(arr) - 1
		id := -1

		for left <= right {
			middle := (left + right) / 2
			if arr[middle][0] < start {
				left = middle + 1
			} else {
				id = middle
				right = middle - 1
			}
		}

		if id == -1 {
			return arr[len(arr)-1][2] + start
		}

		if id == 0 {
			return arr[0][3]
		}

		return min(
			arr[id-1][2]+start,
			arr[id][3],
		)
	}

	res := inf
	// land first
	for i := range n {
		end := landArr[i][0] + landArr[i][1]
		res = min(res, getMinEnd(waterArr, end))
	}
	// water first
	for i := range m {
		end := waterArr[i][0] + waterArr[i][1]
		res = min(res, getMinEnd(landArr, end))
	}

	return res
}

func main() {
	fmt.Println("earliestFinishTime...")
	// call your solution here

}
