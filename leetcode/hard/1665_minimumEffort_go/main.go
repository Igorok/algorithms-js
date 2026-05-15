package main

import (
	"cmp"
	"fmt"
	"slices"
)

func minimumEffort(tasks [][]int) int {
	initial := 0
	for i, task := range tasks {
		initial += task[0]
		tasks[i] = append(tasks[i], tasks[i][1]-tasks[i][0])
	}

	slices.SortFunc(tasks, func(a, b []int) int {
		return cmp.Compare(b[2], a[2])
	})

	// fmt.Println(tasks)

	curr := initial
	for _, task := range tasks {
		if curr < task[1] {
			diff := task[1] - curr
			curr += diff
			initial += diff
		}

		curr -= task[0]
	}

	return initial
}

/*


{
	name: "tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]",
	args: InputVal{
		tasks: [][]int{{1, 3}, {2, 4}, {10, 11}, {10, 12}, {8, 9}},
	},
	want: 32,
},

[10,12], 12, 2
[10,11], 2+9 - 10, 0
[8,9] 0+9-8, 1
[1,3], 1+2-3, 0
[2,4], 0+4-2 = 2

12+9+9+2+4 = 36
31

[10,12], 31-10
[10,11], 21 - 10
[8,9] 11 - 8
[2,4], 3 - 2; 4; 31+1
[1,3], 2 - 1; 3; 32+1
33

[10,12], 31-10
[10,11], 21 - 10
[2,4], 11 - 2
[1,3], 9-1
[8,9], 8-8; 9; 31+1




{
	name: "tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]",
	args: InputVal{
		tasks: [][]int{{1, 7}, {2, 8}, {3, 9}, {4, 10}, {5, 11}, {6, 12}},
	},
	want: 27,
},




*/

func main() {
	fmt.Println("minimumEffort...")
	// call your solution here

}
