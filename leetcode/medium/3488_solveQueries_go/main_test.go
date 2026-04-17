package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums    []int
	queries []int
}

func TestClosestTarget(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want []int
	}{
		{
			name: "nums = [1,3,1,4,1,3,2], queries = [0,3,5]",
			args: InputVal{
				nums:    []int{1, 3, 1, 4, 1, 3, 2},
				queries: []int{0, 3, 5},
			},
			want: []int{2, -1, 3},
		},
		{
			name: "nums = [1,2,3,4], queries = [0,1,2,3]",
			args: InputVal{
				nums:    []int{1, 2, 3, 4},
				queries: []int{0, 1, 2, 3},
			},
			want: []int{-1, -1, -1, -1},
		},
		{
			name: "[17,7,19,16,17,16,16,4,12,5,8,1,2,16,9,5,17,16,17,16]",
			args: InputVal{
				nums:    []int{17,7,19,16,17,16,16,4,12,5,8,1,2,16,9,5,17,16,17,16},
				queries: []int{7,12,9,11,19,15,6,16},
			},
			want: []int{-1,-1,6,-1,2,6,1,2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := solveQueries(tt.args.nums, tt.args.queries); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("solveQueries() = %v, want %v", got, tt.want)
			}
		})
	}
}
