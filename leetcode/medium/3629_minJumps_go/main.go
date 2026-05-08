package main

import (
	"fmt"
)

func primeNums(limit int) []int {
	acc := make([]int, limit+1)
	acc[0] = 1
	acc[1] = 1
	for i := 2; i < len(acc); i++ {
		if acc[i] == 1 {
			continue
		}
		for j := i + i; j < len(acc); j += i {
			acc[j] = 1
		}
	}
	return acc
}

type QueueItem struct {
	id    int
	num   int
	steps int
}

func minJumps(nums []int) int {
	N := len(nums)
	idsByNum := make(map[int][]int)
	limit := 0
	for i, num := range nums {
		limit = max(limit, num)
		exist, ok := idsByNum[num]
		if !ok {
			exist = make([]int, 0, 10)
		}
		idsByNum[num] = append(exist, i)
	}
	primes := primeNums(limit)
	visitedPrimes := make([]int, len(primes))
	visited := make([]int, len(nums))
	visited[0] = 1

	queue := make([]*QueueItem, 0, 1000)
	queue = append(queue, &QueueItem{id: 0, steps: 0, num: nums[0]})

	pushToQueue := func(id, steps int) {
		if id == N || id == -1 {
			return
		}
		if visited[id] == 1 {
			return
		}
		visited[id] = 1
		queue = append(queue, &QueueItem{id: id, steps: steps, num: nums[id]})
	}

	for len(queue) > 0 {
		item := queue[0]
		queue = queue[1:]

		if item.id == N-1 {
			return item.steps
		}

		steps := item.steps + 1

		pushToQueue(item.id+1, steps)
		pushToQueue(item.id-1, steps)

		if primes[item.num] == 0 && visitedPrimes[item.num] == 0 {
			n := item.num
			for n <= limit {
				arr, ok := idsByNum[n]
				visitedPrimes[n] = 1

				n += item.num
				if !ok {
					continue
				}

				for _, nID := range arr {
					pushToQueue(nID, steps)
				}

			}
		}
	}

	return 0
}

func main() {
	fmt.Println("minJumps...")
	// call your solution here

}
