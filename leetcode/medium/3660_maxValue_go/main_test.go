package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestMaxValue(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want []int
	}{
		{
			name: "nums = [2,1,3]",
			args: InputVal{
				nums: []int{2, 1, 3},
			},
			want: []int{2, 2, 3},
		},
		{
			name: "nums = [2,3,1]",
			args: InputVal{
				nums: []int{2, 3, 1},
			},
			want: []int{3, 3, 3},
		},
		{
			name: "nums = [5,2,1,6,3]",
			args: InputVal{
				nums: []int{5, 2, 1, 6, 3},
			},
			want: []int{6, 6, 6, 6, 6},
		},
		{
			name: "nums = [8,5,20,2,21]",
			args: InputVal{
				nums: []int{8, 5, 20, 2, 21},
			},
			want: []int{20, 20, 20, 20, 21},
		},
		{
			name: "nums = [8 6 7 5 8 7]",
			args: InputVal{
				nums: []int{8, 6, 7, 5, 8, 7},
			},
			want: []int{8, 8, 8, 8, 8, 8},
		},
		{
			name: "nums = [19,25,12,21]",
			args: InputVal{
				nums: []int{19, 25, 12, 21},
			},
			want: []int{25, 25, 25, 25},
		},
		{
			name: "nums = [19,25,12,21]",
			args: InputVal{
				nums: []int{19, 25, 12, 26, 21},
			},
			want: []int{26, 26, 26, 26, 26},
		},
		{
			name: "nums = [18,34,16,32,34]",
			args: InputVal{
				nums: []int{18, 34, 16, 32, 34},
			},
			want: []int{34, 34, 34, 34, 34},
		},
		{
			name: "nums = [11,18,11]",
			args: InputVal{
				nums: []int{11, 18, 11},
			},
			want: []int{11, 18, 18},
		},
		{
			name: "nums = [12,23,50,3,62,73,43,74,73]",
			args: InputVal{
				nums: []int{12, 23, 50, 3, 62, 73, 43, 74, 73},
			},
			want: []int{73, 73, 73, 73, 73, 73, 73, 74, 74},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxValue(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maxValue() = %v, want %v", got, tt.want)
			}
		})
	}
}

/*
Do you know leetcode issue - "3660. Jump Game IX"
Can you explain me a description and give an example?


*/
