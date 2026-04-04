package main

import (
	"cmp"
	"fmt"
	"slices"
)

type Robot struct {
	id        int
	health    int
	position  int
	direction string
}

func sortByPos(a *Robot, b *Robot) int {
	return cmp.Compare(a.position, b.position)
}

func sortById(a *Robot, b *Robot) int {
	return cmp.Compare(a.id, b.id)
}

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
	N := len(positions)
	robots := make([]*Robot, N)

	for i := 0; i < N; i++ {
		robots[i] = &Robot{
			id:        i,
			health:    healths[i],
			position:  positions[i],
			direction: string(directions[i]),
		}
	}

	slices.SortFunc(robots, sortByPos)

	// fmt.Println(1, "robots", robots)

	stack := []*Robot{}

	for _, robot := range robots {
		if robot.direction == "L" {
			if len(stack) == 0 || stack[len(stack)-1].direction == "L" {
				stack = append(stack, robot)
				continue
			}

			for len(stack) > 0 && stack[len(stack) - 1].direction == "R" && robot.health > 0 {
				if stack[len(stack)-1].health == robot.health {
					stack = stack[:len(stack)-1]
					robot.health = 0
					break
				} else if stack[len(stack)-1].health > robot.health {
					stack[len(stack)-1].health -= 1
					robot.health = 0
					break
				} else {
					stack = stack[:len(stack)-1]
					robot.health -= 1
				}
			}

			if robot.health > 0 {
				stack = append(stack, robot)
			}

		} else {
			stack = append(stack, robot)
		}

	}

	// fmt.Println(2, "robots", robots)
	// fmt.Println(2, "stack", stack)

	slices.SortFunc(stack, sortById)

	res := make([]int, len(stack))

	for i, robot := range stack {
		res[i] = robot.health
	}

	return res

}

func main() {
	fmt.Println("survivedRobotsHealths...")
	// call your solution here
}
