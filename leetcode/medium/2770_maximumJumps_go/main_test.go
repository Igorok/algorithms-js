package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums   []int
	target int
}

func TestMinJumps(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [1,3,6,4,1,2], target = 2",
			args: InputVal{
				nums:   []int{1, 3, 6, 4, 1, 2},
				target: 2,
			},
			want: 3,
		},
		{
			name: "nums = [1,3,6,4,1,2], target = 3",
			args: InputVal{
				nums:   []int{1, 3, 6, 4, 1, 2},
				target: 3,
			},
			want: 5,
		},
		{
			name: "nums = [1,3,6,4,1,2], target = 0",
			args: InputVal{
				nums:   []int{1, 3, 6, 4, 1, 2},
				target: 0,
			},
			want: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maximumJumps(tt.args.nums, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maximumJumps() = %v, want %v", got, tt.want)
			}
		})
	}
}
