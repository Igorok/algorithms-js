package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestFindMin(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [3,4,5,1,2]",
			args: InputVal{
				nums: []int{3, 4, 5, 1, 2},
			},
			want: 1,
		},
		{
			name: "nums = [4,5,6,7,0,1,2]",
			args: InputVal{
				nums: []int{4, 5, 6, 7, 0, 1, 2},
			},
			want: 0,
		},
		{
			name: "nums = [11,13,15,17]",
			args: InputVal{
				nums: []int{11, 13, 15, 17},
			},
			want: 11,
		},
		{
			name: "nums = [2,1]",
			args: InputVal{
				nums: []int{2, 1},
			},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findMin(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("findMin() = %v, want %v", got, tt.want)
			}
		})
	}
}
