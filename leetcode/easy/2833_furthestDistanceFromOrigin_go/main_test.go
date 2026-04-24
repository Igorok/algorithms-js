package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	moves string
}

func TestFurthestDistanceFromOrigin(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "1",
			args: InputVal{
				moves: "L_RL__R",
			},
			want: 3,
		},
		{
			name: "2",
			args: InputVal{
				moves: "_R__LL_",
			},
			want: 5,
		},
		{
			name: "3",
			args: InputVal{
				moves: "_______",
			},
			want: 7,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := furthestDistanceFromOrigin(tt.args.moves); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("furthestDistanceFromOrigin() = %v, want %v", got, tt.want)
			}
		})
	}
}
