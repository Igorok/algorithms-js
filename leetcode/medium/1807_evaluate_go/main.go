package main

import (
	"fmt"
)


func evaluate(s string, knowledge [][]string) string {
	knowMap := make(map[string]string)
	for _, arr := range knowledge {
		knowMap[arr[0]] = arr[1]
	}

	res := ""
	key := ""
	isOpen := false

	for _, r := range s {
		if string(r) == "(" {
			isOpen = true
			continue
		} else if string(r) == ")" {
			isOpen = false
			val, ok := knowMap[key]
			if ok {
				res = res + val
			} else {
				res = res + "?"
			}
			key = ""
			continue
		}

		if !isOpen {
			res = res + string(r)
		} else {
			key = key + string(r)
		}
	}

	return res
}

func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
