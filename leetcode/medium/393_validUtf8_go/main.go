package main

import (
	"fmt"
)

func generateBits() [5]int {
	var bits = [5]int{}
	for i := 1; i < 5; i++ {
		add := 1 << (8 - i)
		bits[i] = bits[i-1] | add
	}
	return bits
}

var bits = generateBits()

func getByteSize(num int) int {
	shift := 3
	for i := 4; i > -1; i-- {
		n := num >> shift
		n = n << shift
		shift += 1

		// fmt.Println(i, "num", num, strconv.FormatInt(int64(num), 2))
		// fmt.Println(i, "n", n, strconv.FormatInt(int64(n), 2))
		// fmt.Println("bits", bits[i], strconv.FormatInt(int64(bits[i]), 2))

		if bits[i] == n {
			return i
		}
	}

	return -1

}

func validUtf8(data []int) bool {
	length := 0
	cnt := 0

	for _, char := range data {
		size := getByteSize(char)
		if size == -1 {
			return false
		}

		if length == 0 {
			if size == 1 {
				return false
			}

			length = size
			cnt = 1
			continue
		}

		if size != 1 {
			return false
		}

		cnt += 1
		if length == cnt {
			length = 0
			cnt = 0
		}

	}

	return length == 0
}

// 11111111
// 10000000

func main() {
	fmt.Println("validUtf8...")
	// call your solution here

}
