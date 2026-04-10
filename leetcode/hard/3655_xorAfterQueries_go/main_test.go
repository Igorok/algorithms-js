package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums    []int
	queries [][]int
}

func TestSurvivedRobotsHealths(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [1,1,1], queries = [[0,2,1,4]]",
			args: InputVal{
				nums:    []int{1, 1, 1},
				queries: [][]int{{0, 2, 1, 4}},
			},
			want: 4,
		},
		{
			name: "nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]",
			args: InputVal{
				nums:    []int{2, 3, 1, 5, 4},
				queries: [][]int{{1, 4, 2, 3}, {0, 2, 1, 2}},
			},
			want: 31,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := xorAfterQueries(tt.args.nums, tt.args.queries); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("survivedRobotsHealths() = %v, want %v", got, tt.want)
			}
		})
	}
}
