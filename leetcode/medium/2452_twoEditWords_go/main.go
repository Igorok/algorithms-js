package main

import (
	"fmt"
)

type TrieNode struct {
	val      string
	children [26]*TrieNode
	isEnd    bool
}

type QueueItem struct {
	edit int
	id   int
	node *TrieNode
}

func twoEditWords(queries []string, dictionary []string) []string {
	trie := &TrieNode{
		val:      "",
		children: [26]*TrieNode{},
		isEnd:    false,
	}

	for _, word := range dictionary {
		node := trie
		for _, rn := range []rune(word) {
			id := rn - 'a'

			if node.children[id] == nil {
				newNode := TrieNode{
					val:      string(rn),
					children: [26]*TrieNode{},
					isEnd:    false,
				}

				node.children[id] = &newNode
			}

			node = node.children[id]
		}
		node.isEnd = true
	}

	var bfs func(word string) bool
	bfs = func(word string) bool {
		N := len(word)
		queue := make([]*QueueItem, 0, 1000)
		queue = append(queue, &QueueItem{
			id:   0,
			edit: 0,
			node: trie,
		})

		for len(queue) > 0 {
			item := queue[0]
			queue[0] = nil
			queue = queue[1:]

			if item.id == N {
				return true
			}

			charId := int(word[item.id] - 'a')

			for i := range 26 {
				if item.node.children[i] == nil {
					continue
				}

				if charId == i {
					queue = append(queue, &QueueItem{
						id:   item.id + 1,
						edit: item.edit,
						node: item.node.children[i],
					})
				} else if item.edit < 2 {
					queue = append(queue, &QueueItem{
						id:   item.id + 1,
						edit: item.edit + 1,
						node: item.node.children[i],
					})
				}
			}

		}

		return false
	}

	res := []string{}

	for _, word := range queries {
		exist := bfs(word)

		if exist {
			res = append(res, word)
		}
	}

	return res
}

func main() {
	fmt.Println("twoEditWords...")
	// call your solution here
}

/*

how can I calculate a position for array in golang, like in python?
id = ord(char) - ord('a')?

*/
