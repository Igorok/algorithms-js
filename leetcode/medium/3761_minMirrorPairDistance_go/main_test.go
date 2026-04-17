package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	nums []int
}

func TestMinMirrorPairDistance(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "nums = [12,21,45,33,54]",
			args: InputVal{
				nums: []int{12, 21, 45, 33, 54},
			},
			want: 1,
		},
		{
			name: "nums = [120,21]",
			args: InputVal{
				nums: []int{120, 21},
			},
			want: 1,
		},
		{
			name: "nums = [21,120]",
			args: InputVal{
				nums: []int{21, 120},
			},
			want: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minMirrorPairDistance(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minMirrorPairDistance() = %v, want %v", got, tt.want)
			}
		})
	}
}
