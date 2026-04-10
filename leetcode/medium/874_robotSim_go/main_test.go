package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	commands  []int
	obstacles [][]int
}

/*
robots = [4], distance = [3], walls = [1,10]
*/

func TestSurvivedRobotsHealths(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "commands = [4,-1,3], obstacles = []",
			args: InputVal{
				commands:  []int{4, -1, 3},
				obstacles: [][]int{},
			},
			want: 25,
		},
		{
			name: "commands = [4,-1,4,-2,4], obstacles = [[2,4]]",
			args: InputVal{
				commands:  []int{4, -1, 4, -2, 4},
				obstacles: [][]int{{2, 4}},
			},
			want: 65,
		},
		{
			name: "commands = [6,-1,-1,6], obstacles = [[0,0]]",
			args: InputVal{
				commands:  []int{6, -1, -1, 6},
				obstacles: [][]int{{0, 0}},
			},
			want: 36,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := robotSim(tt.args.commands, tt.args.obstacles); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("survivedRobotsHealths() = %v, want %v", got, tt.want)
			}
		})
	}
}
