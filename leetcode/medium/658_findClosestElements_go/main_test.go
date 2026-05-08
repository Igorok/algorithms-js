package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	arr []int
	k   int
	x   int
}

func TestFindClosestElements(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want []int
	}{
		{
			name: "arr = [1,2,3,4,5], k = 4, x = 3",
			args: InputVal{
				arr: []int{1, 2, 3, 4, 5},
				k:   4,
				x:   3,
			},
			want: []int{1, 2, 3, 4},
		},
		{
			name: "arr = [1,1,2,3,4,5], k = 4, x = -1",
			args: InputVal{
				arr: []int{1, 1, 2, 3, 4, 5},
				k:   4,
				x:   -1,
			},
			want: []int{1, 1, 2, 3},
		},
		{
			name: "arr = [1,1,1,10,10,10]",
			args: InputVal{
				arr: []int{1, 1, 1, 10, 10, 10},
				k:   1,
				x:   9,
			},
			want: []int{10},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findClosestElements(tt.args.arr, tt.args.k, tt.args.x); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("findClosestElements() = %v, want %v", got, tt.want)
			}
		})
	}
}
