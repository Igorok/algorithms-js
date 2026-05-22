package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums   []int
	target int
}

func TestSearch(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [4,5,6,7,0,1,2], target = 0",
			args: InputVal{
				nums:   []int{4, 5, 6, 7, 0, 1, 2},
				target: 0,
			},
			want: 4,
		},
		{
			name: "nums = [4,5,6,7,0,1,2], target = 3",
			args: InputVal{
				nums:   []int{4, 5, 6, 7, 0, 1, 2},
				target: 3,
			},
			want: -1,
		},
		{
			name: "nums = [1], target = 0",
			args: InputVal{
				nums:   []int{1},
				target: 0,
			},
			want: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := search(tt.args.nums, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("search() = %v, want %v", got, tt.want)
			}
		})
	}
}
