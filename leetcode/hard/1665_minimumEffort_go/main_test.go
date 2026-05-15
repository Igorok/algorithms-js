package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	tasks [][]int
}

func TestMinimumEffort(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "tasks = [[1,2],[2,4],[4,8]]",
			args: InputVal{
				tasks: [][]int{{1, 2}, {2, 4}, {4, 8}},
			},
			want: 8,
		},
		{
			name: "tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]",
			args: InputVal{
				tasks: [][]int{{1, 3}, {2, 4}, {10, 11}, {10, 12}, {8, 9}},
			},
			want: 32,
		},
		{
			name: "tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]",
			args: InputVal{
				tasks: [][]int{{1, 7}, {2, 8}, {3, 9}, {4, 10}, {5, 11}, {6, 12}},
			},
			want: 27,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumEffort(tt.args.tasks); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minimumEffort() = %v, want %v", got, tt.want)
			}
		})
	}
}
