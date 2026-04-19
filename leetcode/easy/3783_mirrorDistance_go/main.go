package main

import (
	"fmt"
	"math"
)

func mirrorDistance(n int) int {
    num := 0
    tmp := n
    for tmp > 0 {
        num = num*10 + tmp % 10
        tmp = tmp / 10
    }
    return int(math.Abs(float64(n) - float64(num)))
}


func main() {
	fmt.Println("maximumAmount...")
	// call your solution here
}
