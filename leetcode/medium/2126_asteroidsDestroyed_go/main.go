package main

import (
	"fmt"
	"slices"
)

func asteroidsDestroyed(mass int, asteroids []int) bool {
	slices.Sort(asteroids)
	curr := mass

	for _, a := range asteroids {
		if a <= curr {
			curr += a
		} else {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("asteroidsDestroyed...")
	// call your solution here

}
