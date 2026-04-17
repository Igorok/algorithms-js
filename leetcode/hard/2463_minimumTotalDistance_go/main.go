package main

import (
	"fmt"
	"math"
	"sort"
)

func minimumTotalDistance(robot []int, factory [][]int) int64 {
	var inf float64 = 1e63

	sort.Slice(robot, func(i, j int) bool {
		return robot[i] < robot[j]
	})
	sort.Slice(factory, func(i, j int) bool {
		return factory[i][0] < factory[j][0]
	})

	factories := []int{}
	for _, fact := range factory {
		for i := 0; i < fact[1]; i++ {
			factories = append(factories, fact[0])
		}
	}

	memo := make(map[int]map[int]float64)

	var rec func(robotId int, factId int) float64
	rec = func(robotId int, factId int) float64 {
		if robotId == -1 {
			return 0
		}
		if factId == -1 {
			return inf
		}

		_, ok := memo[robotId]
		if !ok {
			memo[robotId] = make(map[int]float64)
		}
		cached, ok := memo[robotId][factId]
		if ok {
			return cached
		}


		getFactory := math.Abs(float64(robot[robotId]) - float64(factories[factId]))
		getFactory += rec(robotId-1, factId-1)

		notGetFactory := rec(robotId, factId-1)

		memo[robotId][factId] = min(getFactory, notGetFactory)

		return memo[robotId][factId]
	}

	res := rec(len(robot)-1, len(factories)-1)

	return int64(res)
}

func main() {
	fmt.Println("minimumTotalDistance...")
	// call your solution here
}

/*

- - - x - - - x - - -
y - y - - y -y - - -
*/
