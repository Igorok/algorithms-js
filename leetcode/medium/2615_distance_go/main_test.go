package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestDistance(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want []int64
	}{
		{
			name: "nums = [1,3,1,1,2]",
			args: InputVal{
				nums: []int{1, 3, 1, 1, 2},
			},
			want: []int64{5, 0, 3, 4, 0},
		},
		{
			name: "nums = [0,5,3]",
			args: InputVal{
				nums: []int{0, 5, 3},
			},
			want: []int64{0, 0, 0},
		},
		{
			name: "nums = [2,0,2,2,6,5,2]",
			args: InputVal{
				nums: []int{2, 0, 2, 2, 6, 5, 2},
			},
			want: []int64{11, 0, 7, 7, 0, 0, 13},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := distance(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("distance() = %v, want %v", got, tt.want)
			}
		})
	}
}
