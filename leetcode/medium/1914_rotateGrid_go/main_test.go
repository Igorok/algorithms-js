package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	grid [][]int
	k    int
}

func TestRotateGrid(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want [][]int
	}{
		{
			name: "grid = [[40,10],[30,20]], k = 1",
			args: InputVal{
				grid: [][]int{{40, 10}, {30, 20}},
				k:    1,
			},
			want: [][]int{{10, 20}, {40, 30}},
		},
		{
			name: "grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2",
			args: InputVal{
				grid: [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}},
				k:    2,
			},
			want: [][]int{{3, 4, 8, 12}, {2, 11, 10, 16}, {1, 7, 6, 15}, {5, 9, 13, 14}},
		},
		{
			name: "3",
			args: InputVal{
				grid: [][]int{{4,5,8,9,4,2,4,7,2,4},{7,1,9,6,6,1,4,5,7,7},{7,1,5,1,1,7,10,1,3,1},{7,2,2,5,2,6,6,4,7,7},{1,2,3,8,4,7,6,9,6,2},{5,10,3,4,7,2,7,5,3,10}},
				k:    4,
			},
			want: [][]int{{4,2,4,7,2,4,7,1,7,2},{9,1,4,5,7,3,7,6,9,10},{8,6,10,1,4,6,6,2,6,3},{5,6,7,1,1,5,2,5,7,5},{4,9,1,1,2,2,3,8,4,7},{7,7,7,1,5,10,3,4,7,2}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := rotateGrid(tt.args.grid, tt.args.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("rotateGrid() = %v, want %v", got, tt.want)
			}
		})
	}
}
