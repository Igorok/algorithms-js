package main

import (
	"fmt"
	"strings"
)

func getIndexByWords(words []string) map[string][]int {
	indexByWord := make(map[string][]int)

	for i, word := range words {
		ids, ok := indexByWord[word]
		if !ok {
			indexByWord[word] = []int{i}
		} else {
			indexByWord[word] = append(ids, i)
		}
	}
	return indexByWord
}

func getLeftId(ids []int, id int) int {
	if len(ids) == 0 {
		return -1
	}
	start := 0
	end := len(ids) - 1
	res := end

	for start <= end {
		middle := int((start + end) / 2)
		if ids[middle] <= id {
			res = middle
			start = middle + 1
		} else {
			end = middle - 1
		}
	}

	return res
}

func getRightId(ids []int, id int) int {
	if len(ids) == 0 {
		return -1
	}
	start := 0
	end := len(ids) - 1
	res := 0

	for start <= end {
		middle := int((start + end) / 2)
		if ids[middle] >= id {
			res = middle
			end = middle - 1
		} else {
			start = middle + 1
		}
	}

	return res
}

// таргет это всего 1 слово а не предложение, надо было пройтись циклом 1 раз
func closestTarget(words []string, target string, startIndex int) int {
	N := len(words)
	indexByWord := getIndexByWords(words)

	targetWords := strings.Fields(target)
	wordsCnt := make(map[string]int)
	for _, word := range targetWords {
		cnt, ok := wordsCnt[word]
		if !ok {
			wordsCnt[word] = 1
		} else {
			wordsCnt[word] = cnt + 1
		}

		exist, ok := indexByWord[word]
		if !ok || len(exist) < wordsCnt[word] {
			return -1
		}
	}

	// travel right
	currId := startIndex
	res1 := 0
	for _, word := range targetWords {
		id := getRightId(indexByWord[word], currId)
		nextId := indexByWord[word][id]
		indexByWord[word] = append(indexByWord[word][:id], indexByWord[word][id+1:]...)
		if nextId >= currId {
			res1 += nextId - currId
		} else {
			res1 += N - currId + nextId
		}
		currId = nextId
	}

	// reload
	indexByWord = getIndexByWords(words)
	// travel left
	currId = startIndex
	res2 := 0
	for _, word := range targetWords {
		id := getLeftId(indexByWord[word], currId)
		nextId := indexByWord[word][id]
		indexByWord[word] = append(indexByWord[word][:id], indexByWord[word][id+1:]...)
		if nextId <= currId {
			res2 += currId - nextId
		} else {
			res2 += N - nextId + currId
		}
		currId = nextId
	}

	return min(res1, res2)
}

func main() {
	fmt.Println("minimumTotalDistance...")
	// call your solution here
}
