package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	robots   []int
	distance []int
	walls    []int
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
			name: "robots = [4], distance = [3], walls = [1,10]",
			args: InputVal{
				robots:   []int{4},
				distance: []int{3},
				walls:    []int{1, 10},
			},
			want: 1,
		},
		{
			name: "robots = [10,2], distance = [5,1], walls = [5,2,7]",
			args: InputVal{
				robots:   []int{10, 2},
				distance: []int{5, 1},
				walls:    []int{5, 2, 7},
			},
			want: 3,
		},
		{
			name: "robots = [1,2], distance = [100,1], walls = [10]",
			args: InputVal{
				robots:   []int{1, 2},
				distance: []int{100, 1},
				walls:    []int{10},
			},
			want: 0,
		},
		{
			name: "[17,59,32,11,72,18]",
			args: InputVal{
				robots:   []int{17, 59, 32, 11, 72, 18},
				distance: []int{5, 7, 6, 5, 2, 10},
				walls:    []int{17, 25, 33, 29, 54, 53, 18, 35, 39, 37, 20, 14, 34, 13, 16, 58, 22, 51, 56, 27, 10, 15, 12, 23, 45, 43, 21, 2, 42, 7, 32, 40, 8, 9, 1, 5, 55, 30, 38, 4, 3, 31, 36, 41, 57, 28, 11, 49, 26, 19, 50, 52, 6, 47, 46, 44, 24, 48},
			},
			want: 37,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxWalls(tt.args.robots, tt.args.distance, tt.args.walls); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("survivedRobotsHealths() = %v, want %v", got, tt.want)
			}
		})
	}
}
