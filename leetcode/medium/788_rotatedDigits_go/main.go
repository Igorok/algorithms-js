package main

import (
	"fmt"
	"strconv"
	"strings"
)

var rotatedMap = map[rune]string{
	'0': "0",
	'1': "1",
	'2': "5",
	'5': "2",
	'6': "9",
	'8': "8",
	'9': "6",
}

func rotate(str string) string {
	res := make([]string, len(str))
	for i, val := range str {
		res[i] = rotatedMap[val]
	}
	return strings.Join(res, "")
}

func rotatedDigits(n int) int {
	res := 0

	var rec func(acc string)
	rec = func(acc string) {
		if len(acc) > 0 {
			num, _ := strconv.Atoi(acc)
			if num > n {
				return
			}
		}

		rot := rotate(acc)
		if rot != acc {
			res += 1
		}

		for _, v := range rotatedMap {
			if len(acc) == 0 && v == "0" {
				continue
			}
			rec(acc + v)
		}
	}

	rec("")

	return res
}

func rotatedDigits_0(n int) int {
	rotatedMap := map[rune]string{
		'0': "0",
		'1': "1",
		'2': "5",
		'3': "-",
		'4': "-",
		'5': "2",
		'6': "9",
		'7': "-",
		'8': "8",
		'9': "6",
	}
	res := 0

	for curr := 2; curr <= n; curr++ {
		str := strconv.Itoa(curr)
		length := len(str)
		rotated := make([]string, length)
		success := true

		for i, val := range str {
			rot := rotatedMap[val]
			if rot == "-" {
				success = false
				break
			}
			rotated[i] = rot
		}

		if success && strings.Join(rotated, "") != str {
			res += 1
		}

	}

	return res
}

func main() {
	fmt.Println("rotatedDigits...")
	// call your solution here
}
