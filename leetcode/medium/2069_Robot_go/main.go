package main

import (
	"fmt"
)

type Robot struct {
	Width     int
	Height    int
	X         int
	Y         int
	Direction int
}

var shifts [][]int = [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
var dirNames = map[int]string{
	0: "North",
	1: "East",
	2: "South",
	3: "West",
}

func Constructor(width int, height int) Robot {
	return Robot{
		Width:     width,
		Height:    height,
		X:         0,
		Y:         0,
		Direction: 1,
	}
}

func (this *Robot) Step(num int) {
	total := 2*(this.Width-1 + this.Height-1)

	if this.Y == 0 && this.X == 0 && num >= total {
		this.Direction = 2
	}

	num = num % total


	for num > 0 {
		shift := shifts[this.Direction]
		newY := this.Y + shift[0]*num
		newX := this.X + shift[1]*num

		if newY < 0 || newY >= this.Height || newX < 0 || newX >= this.Width {
			diff := 0

			switch this.Direction {
			case 0:
				diff = this.Height - 1 - this.Y
			case 1:
				diff = this.Width - 1 - this.X
			case 2:
				diff = this.Y
			default:
				diff = this.X
			}

			this.Y += shift[0] * diff
			this.X += shift[1] * diff
			num -= diff

			this.Direction -= 1
			if this.Direction == -1 {
				this.Direction = 3
			}

			continue
		}

		this.Y = newY
		this.X = newX
		num = 0

	}


}

func (this *Robot) GetPos() []int {
	return []int{this.X, this.Y}
}

func (this *Robot) GetDir() string {
	return dirNames[this.Direction]
}

/**
 * Your Robot object will be instantiated and called as such:
 * obj := Constructor(width, height);
 * obj.Step(num);
 * param_2 := obj.GetPos();
 * param_3 := obj.GetDir();
 */

func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
