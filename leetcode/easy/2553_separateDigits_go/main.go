package main

import (
	"fmt"
)

func separateDigits(nums []int) []int {
	res := make([]int, 0, len(nums))

	for _, num := range nums {
		arr := []int{}
		n := num
		for n > 0 {
			arr = append(arr, n%10)
			n = n / 10
		}
		for i := len(arr) - 1; i > -1; i-- {
			res = append(res, arr[i])
		}
	}

	return res
}

type MyCircularQueue struct {
	queue  []int
	length int
	left   int
	cnt    int
}

func Constructor(k int) MyCircularQueue {
	mcq := MyCircularQueue{
		length: k,
		left:   0,
		cnt:    0,
		queue:  make([]int, k),
	}
	return mcq
}

func (this *MyCircularQueue) EnQueue(value int) bool {
	if this.IsFull() {
		return false
	}
	right := (this.left + this.cnt) % this.length
	this.cnt += 1
	this.queue[right] = value
	return true
}

func (this *MyCircularQueue) DeQueue() bool {
	if this.IsEmpty() {
		return false
	}
	this.left += 1
	this.cnt -= 1
	return true
}

func (this *MyCircularQueue) Front() int {
	if this.IsEmpty() {
		return -1
	}
	return this.queue[this.left%this.length]
}

func (this *MyCircularQueue) Rear() int {
	if this.IsEmpty() {
		return -1
	}
	right := (this.left + this.cnt - 1) % this.length
	return this.queue[right]
}

func (this *MyCircularQueue) IsEmpty() bool {
	return this.cnt == 0
}

func (this *MyCircularQueue) IsFull() bool {
	return this.cnt == this.length
}

func main() {
	fmt.Println("separateDigits...")
	// call your solution here

	// mcq := Constructor(3)
	// fmt.Println(mcq.EnQueue(1))
	// fmt.Println(mcq.EnQueue(2))
	// fmt.Println(mcq.EnQueue(3))
	// fmt.Println(mcq.EnQueue(4))
	// fmt.Println(mcq.Rear())
	// fmt.Println(mcq.IsFull())
	// fmt.Println(mcq.DeQueue())
	// fmt.Println(mcq.EnQueue(4))
	// fmt.Println(mcq.Rear())

	// mcq := Constructor(8)
	// fmt.Println(mcq.EnQueue(3))
	// fmt.Println(mcq.EnQueue(9))
	// fmt.Println(mcq.EnQueue(5))
	// fmt.Println(mcq.EnQueue(0))
	// fmt.Println(mcq.DeQueue())
	// fmt.Println(mcq.DeQueue())
	// fmt.Println(mcq.IsEmpty())
	// fmt.Println(mcq.IsEmpty())
	// fmt.Println(mcq.Rear())
	// fmt.Println(mcq.Rear())
	// fmt.Println(mcq.DeQueue())

	mcq := Constructor(2)
	fmt.Println(mcq.EnQueue(1))
	fmt.Println(mcq.EnQueue(2))
	fmt.Println(mcq.DeQueue())
	fmt.Println(mcq.EnQueue(3))
	fmt.Println(mcq.DeQueue())
	fmt.Println(mcq.EnQueue(3))
	fmt.Println(mcq.DeQueue())
	fmt.Println(mcq.EnQueue(3))
	fmt.Println(mcq.Front())
}
