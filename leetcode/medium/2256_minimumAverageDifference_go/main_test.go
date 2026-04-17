package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestMinimumAverageDifference(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [2,5,3,9,5,3]",
			args: InputVal{
				nums: []int{2, 5, 3, 9, 5, 3},
			},
			want: 3,
		},
		{
			name: "nums = [0]",
			args: InputVal{
				nums: []int{0},
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumAverageDifference(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minimumAverageDifference() = %v, want %v", got, tt.want)
			}
		})
	}
}
