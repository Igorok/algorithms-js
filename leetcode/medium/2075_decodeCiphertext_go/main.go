package main

import (
	"fmt"
	"math"
	"strings"
)

func decodeCiphertext(encodedText string, rows int) string {
	chars := strings.Split(encodedText, "")

	length := len(chars)
	if length == 0 {
		return ""
	}
	cols := int(math.Round(float64(length) / float64(rows)))

	res := []string{}
	for col := range cols {
		c := col
		for row := range rows {
			id := row*cols + c
			c += 1
			if id >= length {
				break
			}
			val := chars[id]
			res = append(res, string(val))
		}
	}
	
	for len(res) > 0 && string(res[len(res)-1]) == " " {
		res = res[:len(res)-1]
	}

	ans := strings.Join(res, "")
	return ans
}

func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}

/*


wammikhefewmfr bjdmdvhszfaaiazvubzphgbiuaofogvxyzycjiswtmarrrdtqacsetahqcz ahfqdfzrithwjobijz oyiwllwy, 
want 
wammikhefewmfr  bjdmdvhszfaaiazvubzphgbiuaofogvxyzycjiswtmarrrdtqacsetahqcz ahfqdfzrithwjobijz oyiwllwy




 */
