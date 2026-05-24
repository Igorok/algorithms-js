package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestMinIncrementForUnique(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [1,2,2]",
			args: InputVal{
				nums: []int{1, 2, 2},
			},
			want: 1,
		},
		{
			name: "nums = [3,2,1,2,1,7]",
			args: InputVal{
				nums: []int{3, 2, 1, 2, 1, 7},
			},
			want: 6,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minIncrementForUnique(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minIncrementForUnique() = %v, want %v", got, tt.want)
			}
		})
	}
}
