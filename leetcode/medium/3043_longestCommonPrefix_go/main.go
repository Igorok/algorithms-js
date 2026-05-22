package main

import (
	"fmt"
	"strconv"
)

type TrieNode struct {
	child []*TrieNode
	val   rune
}

func longestCommonPrefix(arr1 []int, arr2 []int) int {
	root := &TrieNode{val: -1, child: make([]*TrieNode, 10)}

	for _, num := range arr1 {
		node := root

		str := strconv.Itoa(num)
		for _, r := range str {
			id := r - '0'
			if node.child[id] != nil {
				node = node.child[id]
				continue
			}
			node.child[id] = &TrieNode{val: id, child: make([]*TrieNode, 10)}
			node = node.child[id]
		}
	}

	res := 0
	for _, num := range arr2 {
		i := 0
		node := root
		str := strconv.Itoa(num)

		for _, r := range str {
			id := r - '0'
			if node.child[id] != nil {
				node = node.child[id]
				i += 1
				continue
			}
			break
		}

		res = max(res, i)
	}

	// fmt.Println("root", root)

	return res
}

func main() {
	fmt.Println("longestCommonPrefix...")
	// call your solution here

}
