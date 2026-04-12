package main

import (
	"fmt"
	"math"
)

func minimumDistance(word string) int {
	txt := []rune(word)
	N := len(txt)

	memo := make(map[int]map[int]int)

	// fmt.Println("memo", memo)

	// fmt.Println("txt", txt)

	locByChar := make(map[string][]int)
	id := 0
	for i := 'A'; i <= 'Z'; i++ {
		locByChar[string(i)] = []int{int(id / 6), id % 6}
		id += 1
	}
	// fmt.Println(locByChar)

	var getDist func(id1, id2 int) int
	getDist = func(id1, id2 int) int {
		if id1 == -1 || id2 == -1 {
			return 0
		}
		char1 := locByChar[string(txt[id1])]
		char2 := locByChar[string(txt[id2])]
		return int(math.Abs(float64(char1[0])-float64(char2[0])) + math.Abs(float64(char1[1])-float64(char2[1])))
	}

	var rec func(id1 int, id2 int) int
	rec = func(id1 int, id2 int) int {
		nextId := max(id1, id2) + 1
		if nextId == N {
			return 0
		}

		_, ok := memo[id1]
		if !ok {
			memo[id1] = make(map[int]int)
		} else {
			val, ok := memo[id1][id2]
			if !ok {
				memo[id1][id2] = -1
			} else {
				return val
			}
		}

		dist1 := int(10e9)
		dist2 := int(10e9)
		dist3 := int(10e9)
		dist4 := int(10e9)
		// id1
		dist1 = getDist(id1, nextId) + rec(nextId, id2)
		// id2
		dist2 = getDist(id2, nextId) + rec(id1, nextId)
		if nextId+1 < N {
			// id1 + id2
			dist3 = getDist(id1, nextId) + getDist(id2, nextId+1) + rec(nextId, nextId+1)
			// id2 + id1
			dist4 = getDist(id1, nextId+1) + getDist(id2, nextId) + rec(nextId+1, nextId)
		}

		memo[id1][id2] = min(dist1, dist2, dist3, dist4)

		return memo[id1][id2]
	}

	return rec(-1, -1)

}


func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
