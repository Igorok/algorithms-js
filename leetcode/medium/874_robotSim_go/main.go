package main

import (
	"fmt"
)

type Point struct {
	x int
	y int
}

func robotSim(commands []int, obstacles [][]int) int {
	shiftByStatus := [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
	changeStatus := func(status int, command int) int {
		if command == -1 {
			return (status + 1) % 4
		}
		status -= 1
		if status == -1 {
			status = 3
		}
		return status
	}

	obstMap := make(map[Point]struct{})
	for _, loc := range obstacles {
		obstMap[Point{x: loc[0], y: loc[1]}] = struct{}{}
	}

	x := 0
	y := 0
	status := 0
	res := 0

	for _, command := range commands {
		if command < 0 {
			status = changeStatus(status, command)
			continue
		}

		for range command {
			shift := shiftByStatus[status]
			newX := x + shift[1]
			newY := y + shift[0]

			p := Point{x: newX, y: newY}
			if _, exist := obstMap[p]; exist {
				break
			}
			x = newX
			y = newY

			res = max(res, (x*x)+(y*y))
		}

	}

	return res
}

func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
