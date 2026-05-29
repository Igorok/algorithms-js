package main

import (
	"fmt"
)

func largestSumOfAverages(nums []int, k int) float64 {
	N := len(nums)
	sumOfNums := make([]int, N)
	memo := make([][]float64, N)

	for i := range N {
		prev := 0
		if i > 0 {
			prev = sumOfNums[i-1]
		}
		sumOfNums[i] = nums[i] + prev

		memo[i] = make([]float64, k+1)
	}

	var rec func(id, groups int) float64
	rec = func(id, groups int) float64 {
		if id == N {
			return 0
		}
		if groups == 0 {
			return 0
		}
		if groups == 1 {
			prev := 0
			if id > 0 {
				prev = sumOfNums[id-1]
			}
			cnt := N - id
			memo[id][groups] = float64(sumOfNums[N-1]-prev) / float64(cnt)
			return memo[id][groups]
		}

		if memo[id][groups] != 0 {
			return memo[id][groups]
		}

		res := float64(-1)
		for i := id; i < N; i++ {
			prev := 0
			if id > 0 {
				prev = sumOfNums[id-1]
			}
			currSum := sumOfNums[i] - prev
			cnt := i + 1 - id
			avg := float64(currSum) / float64(cnt)

			r := rec(i+1, groups-1)
			res = max(res, r+avg)
		}

		memo[id][groups] = res
		return memo[id][groups]

	}

	return rec(0, k)
}

func main() {
	fmt.Println("largestSumOfAverages...")
	// call your solution here

}

/*

do you know this leetcode issue - "3093. Longest Common Suffix Queries"
description tell about suffix, i try a test case

wordsContainer
["abcdefgh","poiuygh","ghghgh"]
wordsQuery = ["abc"]
I have an answer 2
but


*/
