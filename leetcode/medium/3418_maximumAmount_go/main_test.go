package main

import (
	"reflect"
	"testing"
)

/*
[
[0,1,-1],
[1,-2,3],
[2,-3,4]
]


[
[[0 0 0] [1 2 2] [0 0 0]]
[[1 2 2] [-1 -2 -2] [3 6 6]]
[[3 6 6] [0 0 0] [7 14 14]]
]
*/

func TestSurvivedRobotsHealths(t *testing.T) {
	tests := []struct {
		name string
		args [][]int
		want int
	}{
		{
			name: "coins = [[0,1,-1],[1,-2,3],[2,-3,4]]",
			args: [][]int{
				[]int{0, 1, -1},
				[]int{1, -2, 3},
				[]int{2, -3, 4},
			},
			want: 8,
		},
		{
			name: "coins = [[10,10,10],[10,10,10]]",
			args: [][]int{
				[]int{10, 10, 10},
				[]int{10, 10, 10},
			},
			want: 40,
		},
		{
			name: "[[0,1,-1],[1,2,-3],[-3,-3,-3],[-3,-3,-3],[-3,-3,-3],[-3,-3,-3],[-3,-3,3],[-3,-2,3],[2,-3,4]]",
			args: [][]int{
				[]int{0, 1, -1},
				[]int{1, 2, -3},
				[]int{-3, -3, -3},
				[]int{-3, -3, -3},
				[]int{-3, -3, -3},
				[]int{-3, -3, -3},
				[]int{-3, -3, 3},
				[]int{-3, -2, 3},
				[]int{2, -3, 4},
			},
			want: 4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maximumAmount(tt.args); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("survivedRobotsHealths() = %v, want %v", got, tt.want)
			}
		})
	}
}
