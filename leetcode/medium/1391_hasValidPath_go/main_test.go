package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	grid [][]int
}

func TestHasValidPath(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want bool
	}{
		{
			name: "1",
			args: InputVal{
				grid: [][]int{{2, 4, 3}, {6, 5, 2}},
			},
			want: true,
		},
		{
			name: "2",
			args: InputVal{
				grid: [][]int{{1, 2, 1}, {1, 2, 1}},
			},
			want: false,
		},
		{
			name: "3",
			args: InputVal{
				grid: [][]int{{1, 1, 2}},
			},
			want: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := hasValidPath(tt.args.grid); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("hasValidPath() = %v, want %v", got, tt.want)
			}
		})
	}
}
