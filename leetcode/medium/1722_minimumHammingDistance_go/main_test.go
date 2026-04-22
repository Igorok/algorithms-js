package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	source       []int
	target       []int
	allowedSwaps [][]int
}

func TestMaxDistance(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]",
			args: InputVal{
				source:       []int{1, 2, 3, 4},
				target:       []int{2, 1, 4, 5},
				allowedSwaps: [][]int{[]int{0, 1}, []int{2, 3}},
			},
			want: 1,
		},
		{
			name: "source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []",
			args: InputVal{
				source:       []int{1, 2, 3, 4},
				target:       []int{1, 3, 2, 4},
				allowedSwaps: [][]int{},
			},
			want: 2,
		},
		{
			name: "source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]",
			args: InputVal{
				source:       []int{5, 1, 2, 4, 3},
				target:       []int{1, 5, 4, 2, 3},
				allowedSwaps: [][]int{[]int{0, 4}, []int{4, 2}, []int{1, 3}, []int{1, 4}},
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumHammingDistance(tt.args.source, tt.args.target, tt.args.allowedSwaps); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minimumHammingDistance() = %v, want %v", got, tt.want)
			}
		})
	}
}
