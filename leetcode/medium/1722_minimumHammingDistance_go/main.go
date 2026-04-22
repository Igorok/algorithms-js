package main

import (
	"fmt"
)

type Union struct {
	parents    []int
	nodesCount []int
}

func newUnion(length int) *Union {
	u := Union{}

	u.parents = make([]int, length)
	u.nodesCount = make([]int, length)
	for id, _ := range u.parents {
		u.parents[id] = -1
	}

	return &u
}

func (u *Union) getParent(id int) int {
	if u.parents[id] == -1 {
		u.parents[id] = id
		u.nodesCount[id] = 1
		return id
	}

	if u.parents[id] == id {
		return id
	}

	parent := u.getParent(u.parents[id])
	u.parents[id] = parent
	return parent
}

func (u *Union) setParent(id1, id2 int) {
	parent1 := u.getParent(id1)
	cnt1 := u.nodesCount[parent1]

	parent2 := u.getParent(id2)
	cnt2 := u.nodesCount[parent2]

	if cnt1 >= cnt2 {
		u.nodesCount[parent1] += u.nodesCount[parent2]
		u.parents[parent2] = parent1
	} else {
		u.nodesCount[parent2] += u.nodesCount[parent1]
		u.parents[parent1] = parent2
	}
}

func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int) int {
	N := len(source)
	union := newUnion(N)

	for _, swap := range allowedSwaps {
		union.setParent(swap[0], swap[1])
	}

	cntOfNums := make(map[int]map[int]int)

	for id, num := range source {
		parent := union.getParent(id)
		_, ok := cntOfNums[parent]
		if !ok {
			cntOfNums[parent] = make(map[int]int)
		}
		cntOfNums[parent][num] += 1
	}

	res := 0
	for id, num := range target {
		parent := union.getParent(id)
		exist, ok := cntOfNums[parent][num]
		if !ok || exist == 0 {
			res += 1
			continue
		}
		cntOfNums[parent][num] -= 1
	}

	return res
}

func main() {
	fmt.Println("minimumHammingDistance...")
	// call your solution here
}
