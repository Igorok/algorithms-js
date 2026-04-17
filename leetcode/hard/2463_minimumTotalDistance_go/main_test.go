package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	robot   []int
	factory [][]int
}

func TestMinimumTotalDistance(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int64
	}{
		{
			name: "robot = [0,4,6], factory = [[2,2],[6,2]]",
			args: InputVal{
				robot:   []int{0, 4, 6},
				factory: [][]int{{2, 2}, {6, 2}},
			},
			want: int64(4),
		},
		{
			name: "robot = [1,-1], factory = [[-2,1],[2,1]]",
			args: InputVal{
				robot:   []int{1, -1},
				factory: [][]int{{-2, 1}, {2, 1}},
			},
			want: int64(2),
		},
		{
			name: "3",
			args: InputVal{
				robot:   []int{0, 2, 3},
				factory: [][]int{{0, 3}, {100, 3}},
			},
			want: int64(5),
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumTotalDistance(tt.args.robot, tt.args.factory); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minimumTotalDistance() = %v, want %v", got, tt.want)
			}
		})
	}
}
