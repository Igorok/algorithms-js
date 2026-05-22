package main

import (
	"container/heap"
	"fmt"
)

type HeapItem struct {
	Id    int
	Steps int
	Prev  int
}

// IntHeap is a min-heap of ints.
type MinHeap []*HeapItem

// 1. Len is part of sort.Interface.
func (h MinHeap) Len() int { return len(h) }

// 2. Less is part of sort.Interface.
// For a min-heap, we use elements[i] < elements[j].
// For a max-heap, you would change this to >.
func (h MinHeap) Less(i, j int) bool { return h[i].Steps < h[j].Steps }

// 3. Swap is part of sort.Interface.
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

// 4. Push adds an element to the heap.
// It takes a pointer receiver because it modifies the slice's length.
func (h *MinHeap) Push(x any) {
	*h = append(*h, x.(*HeapItem))
}

// 5. Pop removes and returns the minimum element (the root).
// It also takes a pointer receiver.
func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func minJumps(arr []int) int {
	var inf int = 1e9
	idsByVal := make(map[int][]int)
	for i, num := range arr {
		exist, ok := idsByVal[num]
		if !ok {
			exist = []int{}
		}
		idsByVal[num] = append(exist, i)
	}

	N := len(arr)
	acc := make([]int, N)
	for i := range N {
		acc[i] = inf
	}

	h := &MinHeap{&HeapItem{Id: 0, Steps: 0, Prev: -1}}
	// Initialize the heap invariant (heapify the slice)
	heap.Init(h)

	for h.Len() > 0 {
		item := heap.Pop(h)
		heapItem, ok := item.(*HeapItem)
		if !ok {
			return inf
		}

		if heapItem.Id == N-1 {
			return heapItem.Steps
		}

		if heapItem.Id-1 > -1 && acc[heapItem.Id-1] > heapItem.Steps+1 {
			acc[heapItem.Id-1] = heapItem.Steps + 1
			heap.Push(h, &HeapItem{Id: heapItem.Id - 1, Steps: heapItem.Steps + 1, Prev: heapItem.Id})
		}

		if heapItem.Id+1 < N && acc[heapItem.Id+1] > heapItem.Steps+1 {
			acc[heapItem.Id+1] = heapItem.Steps + 1
			heap.Push(h, &HeapItem{Id: heapItem.Id + 1, Steps: heapItem.Steps + 1, Prev: heapItem.Id})
		}

		if heapItem.Prev == -1 || arr[heapItem.Id] != arr[heapItem.Prev] {
			for _, i := range idsByVal[arr[heapItem.Id]] {
				if i == heapItem.Id || acc[i] <= heapItem.Steps+1 {
					continue
				}
				acc[i] = heapItem.Steps + 1
				heap.Push(h, &HeapItem{Id: i, Steps: heapItem.Steps + 1, Prev: heapItem.Id})
			}
		}

	}

	return inf
}

func main() {
	fmt.Println("minJumps...")
	// call your solution here

}
