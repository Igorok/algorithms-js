package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	matrix [][]int
}

func TestRotate(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want [][]int
	}{
		{
			name: "matrix = [[1,2,3],[4,5,6],[7,8,9]]",
			args: InputVal{
				matrix: [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
			},
			want: [][]int{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}},
		},
		{
			name: "matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]",
			args: InputVal{
				matrix: [][]int{{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}},
			},
			want: [][]int{{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// if got := rotate(tt.args.matrix); !reflect.DeepEqual(got, tt.want) {
			rotate(tt.args.matrix)
			if !reflect.DeepEqual(tt.args.matrix, tt.want) {
				t.Errorf("rotate() = %v, want %v", tt.args.matrix, tt.want)
			}
		})
	}
}
