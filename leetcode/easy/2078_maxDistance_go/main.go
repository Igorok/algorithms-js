package main

import (
	"container/heap"
	"fmt"
)

type IntHeap [][2]int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i][0] < h[j][0] } // Для Min-Heap
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.([2]int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maxDistance(colors []int) int {
	h := &IntHeap{}
	heap.Init(h)

	unique := make(map[int]struct{})

	res := 0

	for id, color := range colors {
		_, ok := unique[color]
		if !ok {
			unique[color] = struct{}{}
			heap.Push(h, [2]int{id, color})
		}

		if h.Len() == 0 {
			continue
		}
		if h.Len() == 1 && (*h)[0][1] == color {
			continue
		}

		var prev1, prev2 [2]int

		val, ok := heap.Pop(h).([2]int)
		if ok {
			prev1 = val
		}

		if prev1[1] != color {
			res = max(res, id-prev1[0])
			heap.Push(h, prev1)
			continue
		}

		val, ok = heap.Pop(h).([2]int)
		if ok {
			prev2 = val
		}

		res = max(res, id-prev2[0])
		heap.Push(h, prev1)
		heap.Push(h, prev2)

	}

	return res
}

func main() {
	fmt.Println("maxDistance...")
	// call your solution here
}
