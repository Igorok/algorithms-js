package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums [][]int
}

func TestSurvivedRobotsHealths(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]",
			args: InputVal{
				nums: [][]int{{7, 2, 1}, {6, 4, 2}, {6, 5, 3}, {3, 2, 1}},
			},
			want: 15,
		},
		{
			name: "nums = [[1]]",
			args: InputVal{
				nums: [][]int{{1}},
			},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := matrixSum(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("survivedRobotsHealths() = %v, want %v", got, tt.want)
			}
		})
	}
}
