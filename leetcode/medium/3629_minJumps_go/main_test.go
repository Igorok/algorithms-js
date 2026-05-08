package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestMinJumps(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [1,2,4,6]",
			args: InputVal{
				nums: []int{1, 2, 4, 6},
			},
			want: 2,
		},
		{
			name: "nums = [2,3,4,7,9]",
			args: InputVal{
				nums: []int{2, 3, 4, 7, 9},
			},
			want: 2,
		},
		{
			name: "nums = [4,6,5,8]",
			args: InputVal{
				nums: []int{4, 6, 5, 8},
			},
			want: 3,
		},
		{
			name: "nums = [7,5,7]",
			args: InputVal{
				nums: []int{7, 5, 7},
			},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minJumps(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minJumps() = %v, want %v", got, tt.want)
			}
		})
	}
}

/*
Do you know leetcode issue - "3660. Jump Game IX"
Can you explain me a description and give an example?


*/
