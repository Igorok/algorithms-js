package main

import (
	"fmt"
	"unicode"
)

func numberOfSpecialChars(word string) int {
	upper := make([]int, 26)
	lower := make([]int, 26)

	for _, char := range word {
		if char == unicode.ToLower(char) {
			lower[char-'a'] += 1
		}

		if char == unicode.ToUpper(char) {
			upper[char-'A'] += 1
		}
	}

	res := 0
	for i := range len(lower) {
		if upper[i] != 0 && lower[i] != 0 {
			res += 1
		}
	}

	return res
}

func main() {
	fmt.Println("numberOfSpecialChars...")
	// call your solution here

}
