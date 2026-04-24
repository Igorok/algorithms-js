package main

import (
	"fmt"
	"math"
)

type CntOfChars struct {
	left  int
	right int
	any   int
}

func furthestDistanceFromOrigin(moves string) int {
	cntOfChars := CntOfChars{
		left:  0,
		right: 0,
		any:   0,
	}

	for _, rn := range moves {
		if rn == 'L' {
			cntOfChars.left += 1
		} else if rn == 'R' {
			cntOfChars.right += 1
		} else {
			cntOfChars.any += 1
		}
	}

	res := math.Abs(float64(cntOfChars.left)-float64(cntOfChars.right)) + float64(cntOfChars.any)
	return int(res)
}

/*


In production i am working with a web api. And there I have a smal count of parallelism, like 5 request to database or other api. In this case I think shared map is good. And it is difficult to imagin a chanels and waiting group for this.

*/

func main() {
	fmt.Println("furthestDistanceFromOrigin...")
	// call your solution here
}
