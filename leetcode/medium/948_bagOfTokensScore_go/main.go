package main

import (
	"fmt"
	"slices"
)

func bagOfTokensScore(tokens []int, power int) int {
	slices.Sort(tokens)
	
	start := 0
	end := len(tokens)-1
	res := 0
	score := 0
	
	for start <= end {
		if power >= tokens[start] {
			score += 1
			power -= tokens[start]
			start += 1

			res = max(res, score)
			
			continue
		}

		if score > 0 {
			score -= 1
			power += tokens[end]
			end -= 1
			continue
		}

		break
	}

	return res
}

func main() {
	fmt.Println("bagOfTokensScore...")
}
