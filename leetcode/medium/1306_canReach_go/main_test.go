package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	arr   []int
	start int
}

func TestCanReach(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want bool
	}{
		{
			name: "arr = [4,2,3,0,3,1,2], start = 5",
			args: InputVal{
				arr:   []int{4, 2, 3, 0, 3, 1, 2},
				start: 5,
			},
			want: true,
		},
		{
			name: "arr = [4,2,3,0,3,1,2], start = 0",
			args: InputVal{
				arr:   []int{4, 2, 3, 0, 3, 1, 2},
				start: 0,
			},
			want: true,
		},
		{
			name: "arr = [3,0,2,1,2], start = 2",
			args: InputVal{
				arr:   []int{3, 0, 2, 1, 2},
				start: 2,
			},
			want: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := canReach(tt.args.arr, tt.args.start); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("canReach() = %v, want %v", got, tt.want)
			}
		})
	}
}
