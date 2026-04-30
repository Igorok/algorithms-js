package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	grid [][]int
	k    int
}

func TestMaxPathScore(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "grid = [[0, 1],[2, 0]], k = 1",
			args: InputVal{
				grid: [][]int{{0, 1}, {2, 0}},
				k:    1,
			},
			want: 2,
		},
		{
			name: "grid = [[0, 1],[1, 2]], k = 1",
			args: InputVal{
				grid: [][]int{{0, 1}, {1, 2}},
				k:    1,
			},
			want: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxPathScore(tt.args.grid, tt.args.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maxPathScore() = %v, want %v", got, tt.want)
			}
		})
	}
}
