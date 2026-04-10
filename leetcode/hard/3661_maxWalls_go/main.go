package main

import (
	"fmt"
	"slices"
)

func maxWalls(robots []int, distance []int, walls []int) int {
	distForRobot := make(map[int]int)
	for i, r := range robots {
		distForRobot[r] = distance[i]
	}

	slices.Sort(robots)
	slices.Sort(walls)

	// fmt.Println(robots)
	// fmt.Println(distForRobot)
	// fmt.Println(walls)

	N := len(robots)
	M := len(walls)
	leftWalls := make([]int, N)
	rightWalls := make([]int, N)
	maxWalls := make([]int, N)

	getCnt := func(left, right int) int {
		l := 0
		r := M - 1

		rightBorder := -1
		for r >= l {
			m := int((l + r) / 2)
			if walls[m] >= left && walls[m] <= right {
				rightBorder = m
				l = m + 1
			} else if walls[m] < left {
				l = m + 1
			} else {
				r = m - 1
			}
		}

		if rightBorder == -1 {
			return 0
		}

		l = 0
		r = M - 1
		leftBorder := 0
		for r >= l {
			m := int((l + r) / 2)
			if walls[m] >= left && walls[m] <= right {
				leftBorder = m
				r = m - 1
			} else if walls[m] < left {
				l = m + 1
			} else {
				r = m - 1
			}
		}

		return rightBorder - leftBorder + 1
	}

	for i, r := range robots {
		leftWalls[i] = 0
		rightWalls[i] = 0
		maxWalls[i] = 0

		leftBorder := r - distForRobot[r]
		if i > 0 {
			leftBorder = max(leftBorder, robots[i-1]+1)
		}
		leftWalls[i] = getCnt(leftBorder, r)

		rightBorder := r + distForRobot[r]
		if i < N-1 {
			rightBorder = min(rightBorder, robots[i+1]-1)
		}
		rightWalls[i] = getCnt(r, rightBorder)

		if i == 0 {
			continue
		}

		maxWalls[i] = getCnt(robots[i-1], r)
		/*
			1 2 3 r 5 6 r 8
		*/
	}


	// fmt.Println("leftWalls", leftWalls)
	// fmt.Println("rightWalls", rightWalls)
	// fmt.Println("maxWalls", maxWalls)

	prevLeft := leftWalls[0]
	prevRight := rightWalls[0]

	for i := 1; i < N; i++ {
		// shut left
		currLeft := max(
			prevLeft+leftWalls[i],
			prevRight-rightWalls[i-1]+min(maxWalls[i], rightWalls[i-1]+leftWalls[i]),
		)
		// shut right
		currRight := max(
			prevLeft + rightWalls[i],
			prevRight + rightWalls[i],
		)

		prevLeft = currLeft
		prevRight = currRight
	}

	return max(prevLeft, prevRight)
}


/*

[11 17 18 32 59 72]
map[11:5 17:5 18:10 32:6 59:7 72:2]
[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58]

leftWalls
[6 6 1 7 7 0]
rightWalls
[6 1 11 7 0 0]
maxWalls
[0 7 2 15 27 0]

*/

func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
