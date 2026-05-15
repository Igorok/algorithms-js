package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums  []int
	limit int
}

func TestMinMoves(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [1,2,4,3], limit = 4",
			args: InputVal{
				nums:  []int{1, 2, 4, 3},
				limit: 4,
			},
			want: 1,
		},
		{
			name: "nums = [1,2,2,1], limit = 2",
			args: InputVal{
				nums:  []int{1, 2, 2, 1},
				limit: 2,
			},
			want: 2,
		},
		{
			name: "nums = [1,2,1,2], limit = 2",
			args: InputVal{
				nums:  []int{1, 2, 1, 2},
				limit: 2,
			},
			want: 0,
		},
		{
			name: "[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]",
			args: InputVal{
				nums:  []int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
				limit: 1,
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minMoves(tt.args.nums, tt.args.limit); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minMoves() = %v, want %v", got, tt.want)
			}
		})
	}
}
