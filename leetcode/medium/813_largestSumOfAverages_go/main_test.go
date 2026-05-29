package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
	k    int
}

func TestLargestSumOfAverages(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want float64
	}{
		{
			name: "1",
			args: InputVal{
				nums: []int{9, 1, 2, 3, 9},
				k:    3,
			},
			want: 20.00000,
		},
		{
			name: "1",
			args: InputVal{
				nums: []int{1, 2, 3, 4, 5, 6, 7},
				k:    4,
			},
			want: 20.50000,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := largestSumOfAverages(tt.args.nums, tt.args.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("largestSumOfAverages() = %v, want %v", got, tt.want)
			}
		})
	}
}
