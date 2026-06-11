package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	mass      int
	asteroids []int
}

func TestRacecar(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want bool
	}{
		{
			name: "mass = 10, asteroids = [3,9,19,5,21]",
			args: InputVal{
				mass:      10,
				asteroids: []int{3, 9, 19, 5, 21},
			},
			want: true,
		},
		{
			name: "mass = 5, asteroids = [4,9,23,4]",
			args: InputVal{
				mass:      5,
				asteroids: []int{4, 9, 23, 4},
			},
			want: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := asteroidsDestroyed(tt.args.mass, tt.args.asteroids); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("asteroidsDestroyed() = %v, want %v", got, tt.want)
			}
		})
	}
}
