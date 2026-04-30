package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	grid [][]int
	x    int
}

func TestMinOperations(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "grid = [[2,4],[6,8]], x = 2",
			args: InputVal{
				grid: [][]int{{2, 4}, {6, 8}},
				x:    2,
			},
			want: 4,
		},
		{
			name: "grid = [[1,5],[2,3]], x = 1",
			args: InputVal{
				grid: [][]int{{1, 5}, {2, 3}},
				x:    1,
			},
			want: 5,
		},
		{
			name: "grid = [[1,2],[3,4]], x = 2",
			args: InputVal{
				grid: [][]int{{1, 2}, {3, 4}},
				x:    2,
			},
			want: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minOperations(tt.args.grid, tt.args.x); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minOperations() = %v, want %v", got, tt.want)
			}
		})
	}
}
