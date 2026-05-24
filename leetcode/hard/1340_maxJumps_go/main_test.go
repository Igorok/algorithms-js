package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	arr []int
	d   int
}

func TestMaxJumps(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2",
			args: InputVal{
				arr: []int{6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12},
				d:   2,
			},
			want: 4,
		},
		{
			name: "arr = [3,3,3,3,3], d = 3",
			args: InputVal{
				arr: []int{3, 3, 3, 3, 3},
				d:   3,
			},
			want: 1,
		},
		{
			name: "arr = [7,6,5,4,3,2,1], d = 1",
			args: InputVal{
				arr: []int{7, 6, 5, 4, 3, 2, 1},
				d:   1,
			},
			want: 7,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxJumps(tt.args.arr, tt.args.d); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maxJumps() = %v, want %v", got, tt.want)
			}
		})
	}
}
