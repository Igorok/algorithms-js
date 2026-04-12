package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestSurvivedRobotsHealths(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [1,2,1,1,3]",
			args: InputVal{
				nums: []int{1, 2, 1, 1, 3},
			},
			want: 6,
		},
		{
			name: "nums = [1,1,2,3,2,1,2]",
			args: InputVal{
				nums: []int{1, 1, 2, 3, 2, 1, 2},
			},
			want: 8,
		},
		{
			name: "nums = [1]",
			args: InputVal{
				nums: []int{1},
			},
			want: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumDistance(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("survivedRobotsHealths() = %v, want %v", got, tt.want)
			}
		})
	}
}
