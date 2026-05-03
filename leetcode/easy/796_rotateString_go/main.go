package main

import (
	"fmt"
)

func rotateString(s string, goal string) bool {
	for i := range len(s) {
		if s[i:] + s[:i] == goal {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println("rotateString...")
	// call your solution here
}
