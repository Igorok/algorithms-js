package main

import (
	"reflect"
	"testing"
)

func TestSurvivedRobotsHealths(t *testing.T) {
	type args struct {
		positions  []int
		healths    []int
		directions string
	}

	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "Case 1: All Right (No Collisions)",
			args: args{
				positions:  []int{5, 4, 3, 2, 1},
				healths:    []int{2, 17, 9, 15, 10},
				directions: "RRRRR",
			},
			want: []int{2, 17, 9, 15, 10},
		},
		{
			name: "Case 2: Simple Collision",
			args: args{
				positions:  []int{3, 5, 2, 6},
				healths:    []int{10, 10, 15, 12},
				directions: "RLRL",
			},
			want: []int{14},
		},
		{
			name: "1,2,5,6",
			args: args{
				positions:  []int{1, 2, 5, 6},
				healths:    []int{10, 10, 11, 11},
				directions: "RLRL",
			},
			want: []int{},
		},
		{
			name: "13,3",
			args: args{
				positions:  []int{13, 3},
				healths:    []int{17, 2},
				directions: "LR",
			},
			want: []int{16},
		},
		{
			name: "1,36,13,18,49",
			args: args{
				positions:  []int{1, 36, 13, 18, 49},
				healths:    []int{37, 26, 12, 45, 15},
				directions: "RRLLR",
			},
			want: []int{26, 44, 15},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := survivedRobotsHealths(tt.args.positions, tt.args.healths, tt.args.directions); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("survivedRobotsHealths() = %v, want %v", got, tt.want)
			}
		})
	}
}
