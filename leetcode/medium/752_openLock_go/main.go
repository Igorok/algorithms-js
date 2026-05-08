package main

import (
	"fmt"
	"slices"
	"strconv"
	"strings"
)

type QueueItem struct {
	code  []int
	steps int
}

func getValidNum(n int) int {
	if n == -1 {
		return 9
	}
	if n == 10 {
		return 0
	}
	return n
}

func getStrCode(arr *[]int) string {
	strCode := make([]string, 4)
	for i, n := range *arr {
		strCode[i] = strconv.Itoa(n)
	}
	return strings.Join(strCode, "")
}

func openLock(deadends []string, target string) int {
	endMap := make(map[string]struct{})
	for _, val := range deadends {
		endMap[val] = struct{}{}
	}
	_, end := endMap["0000"]
	if end {
		return -1
	}
	_, end = endMap[target]
	if end {
		return -1
	}
	if target == "0000" {
		return 0
	}

	queue := make([]*QueueItem, 0, 1_000_000)
	queue = append(queue, &QueueItem{code: []int{0, 0, 0, 0}, steps: 0})

	visited := make(map[string]int)
	visited["0000"] = 0

	for len(queue) > 0 {
		val := queue[0]
		queue = queue[1:]

		for id := range 4 {
			// plus
			arr := slices.Clone(val.code)
			arr[id] = getValidNum(arr[id] + 1)
			key := getStrCode(&arr)

			if key == target {
				return val.steps + 1
			}
			_, end := endMap[key]
			_, ok := visited[key]
			if !end && !ok {
				visited[key] = val.steps + 1
				queue = append(queue, &QueueItem{code: arr, steps: val.steps + 1})
			}

			// minus
			arr = slices.Clone(val.code)
			arr[id] = getValidNum(arr[id] - 1)
			key = getStrCode(&arr)

			if key == target {
				return val.steps + 1
			}
			_, end = endMap[key]
			_, ok = visited[key]
			if !end && !ok {
				visited[key] = val.steps + 1
				queue = append(queue, &QueueItem{code: arr, steps: val.steps + 1})
			}
		}
	}

	// fmt.Println(visited)

	return -1
}

func main() {
	fmt.Println("openLock...")
	// call your solution here
}
