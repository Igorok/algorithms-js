package main

import (
	"fmt"
)

/*

wordsContainer = [
"abcdefgh",8
"poiuygh",7
"ghghgh"6
],
wordsQuery = [
"gh",
"acbfgh",
"acbfegh"
]

[2,0,2]

*/

type TrieNode struct {
	char      byte
	remainder int
	word      int
	children  []*TrieNode
}

func stringIndices(wordsContainer []string, wordsQuery []string) []int {
	trie := &TrieNode{
		char:      '0',
		remainder: int(1e6),
		word:      -1,
		children:  make([]*TrieNode, 28),
	}

	for wordId, word := range wordsContainer {
		m := len(word)
		node := trie
		if m < node.remainder {
			node.remainder = m
			node.word = wordId
		}

		// fmt.Println(word, m)

		for i := m - 1; i > -1; i-- {
			childId := word[i] - 'a'

			// fmt.Println("i", i, "id", int(childId), "char", string(word[i]))

			if node.children[childId] == nil {
				node.children[childId] = &TrieNode{
					char:      word[i],
					remainder: i,
					word:      wordId,
					children:  make([]*TrieNode, 28),
				}
			}

			node = node.children[childId]

			// fmt.Println(1, "node", node.remainder, node.word, i, wordId)

			if node.remainder > i {
				node.remainder = i
				node.word = wordId
			}

			// fmt.Println(2, "node", node.remainder, node.word)

		}

		if node.children[27] != nil {
			node.children[27] = &TrieNode{
				char:      '*',
				remainder: 0,
				word:      wordId,
			}
		}
	}

	res := make([]int, len(wordsQuery))

	for queryId, word := range wordsQuery {
		// fmt.Println("search", word)

		m := len(word)
		node := trie
		r := node.word

		for i := m - 1; i > -1; i-- {
			childId := word[i] - 'a'

			if node.children[childId] == nil {
				break
			}
			node = node.children[childId]

			// fmt.Println(string(node.char), "node", node.remainder, node.word)

			r = node.word
		}

		res[queryId] = r

	}

	return res
}

func main() {
	fmt.Println("stringIndices...")
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
