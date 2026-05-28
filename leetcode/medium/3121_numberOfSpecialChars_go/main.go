package main

import (
	"fmt"
	"unicode"
)

func numberOfSpecialChars(word string) int {
	upper := make([]int, 26)
	lower := make([]int, 26)

	for _, char := range word {
		l := unicode.ToLower(char)
		u := unicode.ToUpper(char)

		if char == l {
			lower[l-'a'] += 1

			if upper[u-'A'] != 0 {
				upper[u-'A'] = -1
			}
			continue
		}

		if lower[l-'a'] == 0 {
			upper[u-'A'] = -1
			continue
		}

		if upper[u-'A'] != -1 {
			upper[u-'A'] += 1
		}
	}

	res := 0
	for i := range len(upper) {
		if upper[i] > 0 {
			res += 1
		}
	}

	return res
}

/*

AbcbDBdD

*/

func main() {
	fmt.Println("numberOfSpecialChars...")
	// call your solution here

}
