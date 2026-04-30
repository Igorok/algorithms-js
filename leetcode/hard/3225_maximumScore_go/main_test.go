package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	grid [][]int
}

func TestMaximumScore(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]",
			args: InputVal{
				grid: [][]int{{0, 0, 0, 0, 0}, {0, 0, 3, 0, 0}, {0, 1, 0, 0, 0}, {5, 0, 0, 3, 0}, {0, 0, 0, 0, 2}},
			},
			want: 11,
		},
		{
			name: "grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]",
			args: InputVal{
				grid: [][]int{{10, 9, 0, 0, 15}, {7, 1, 0, 8, 0}, {5, 20, 0, 11, 0}, {0, 0, 0, 1, 2}, {8, 12, 1, 10, 3}},
			},
			want: 94,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maximumScore(tt.args.grid); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maximumScore() = %v, want %v", got, tt.want)
			}
		})
	}
}
