package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
	k    int
}

func TestFirstStableIndex(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [5,0,1,4], k = 3",
			args: InputVal{
				nums: []int{5, 0, 1, 4},
				k:    3,
			},
			want: 3,
		},
		{
			name: "[3,2,1], k = 1",
			args: InputVal{
				nums: []int{3, 2, 1},
				k:    1,
			},
			want: -1,
		},
		{
			name: "nums = [0], k = 0",
			args: InputVal{
				nums: []int{0},
				k:    0,
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := firstStableIndex(tt.args.nums, tt.args.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("firstStableIndex() = %v, want %v", got, tt.want)
			}
		})
	}
}
