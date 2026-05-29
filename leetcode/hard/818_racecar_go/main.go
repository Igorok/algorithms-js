package main

import (
	"fmt"
)

type Item struct {
	pos int
	spd int
	stp int
}

func racecar(target int) int {
	queue := make([]*Item, 0, 1000)
	queue = append(queue, &Item{pos: 0, spd: 1, stp: 0})

	visited := make(map[string]struct{})
	visited["0_1"] = struct{}{}

	for len(queue) > 0 {
		item := queue[0]
		queue = queue[1:]

		if target == item.pos {
			return item.stp
		}

		// A
		itm := &Item{
			pos: item.pos + item.spd,
			spd: item.spd * 2,
			stp: item.stp + 1,
		}
		key := fmt.Sprintf("%d_%d", itm.pos, itm.spd)

		if itm.pos < target*2 && !(item.pos < 0 && itm.pos < 0) {
			if _, ok := visited[key]; !ok {
				visited[key] = struct{}{}
				queue = append(queue, itm)
			}
		}

		// R
		spd := item.spd
		if spd > 0 {
			spd = -1
		} else {
			spd = 1
		}
		itm = &Item{
			pos: item.pos,
			spd: spd,
			stp: item.stp + 1,
		}

		key = fmt.Sprintf("%d_%d", itm.pos, itm.spd)
		if _, ok := visited[key]; !ok {
			visited[key] = struct{}{}
			queue = append(queue, itm)
		}

	}

	return 0
}

/*

Do you know a leetcode issue - "818. Race Car"
I have tle, with my bfs solution

*/

func main() {
	fmt.Println("racecar...")
	// call your solution here

}
