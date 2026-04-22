package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestMaxDistance(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "colors = [1,1,1,6,1,1,1]",
			args: InputVal{
				nums: []int{1, 1, 1, 6, 1, 1, 1},
			},
			want: 3,
		},
		{
			name: "colors = [1,8,3,8,3]",
			args: InputVal{
				nums: []int{1, 8, 3, 8, 3},
			},
			want: 4,
		},
		{
			name: "colors = [0,1]",
			args: InputVal{
				nums: []int{0, 1},
			},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxDistance(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maxDistance() = %v, want %v", got, tt.want)
			}
		})
	}
}
