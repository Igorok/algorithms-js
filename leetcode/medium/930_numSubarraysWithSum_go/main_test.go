package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
	goal int
}

func TestNumSubarraysWithSum(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [1,0,1,0,1], goal = 2",
			args: InputVal{
				nums: []int{1, 0, 1, 0, 1},
				goal: 2,
			},
			want: 4,
		},
		{
			name: "nums = [0,0,0,0,0], goal = 0",
			args: InputVal{
				nums: []int{0, 0, 0, 0, 0},
				goal: 0,
			},
			want: 15,
		},
		{
			name: "nums = [0,0,1,0,0], goal = 1",
			args: InputVal{
				nums: []int{0, 0, 1, 0, 0},
				goal: 1,
			},
			want: 9,
		},
		{
			name: "nums = [0,0,1,0,0,1], goal = 1",
			args: InputVal{
				nums: []int{0, 0, 1, 0, 0, 1},
				goal: 1,
			},
			want: 12,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numSubarraysWithSum(tt.args.nums, tt.args.goal); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("numSubarraysWithSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
