package main

import (
	"reflect"
	"testing"
)

type InputVal struct {
	word string
}

func TestMinimumDistance(t *testing.T) {
	tests := []struct {
		name string
		args InputVal
		want int
	}{
		{
			name: "CAKE",
			args: InputVal{
				word: "CAKE",
			},
			want: 3,
		},
		{
			name: "HAPPY",
			args: InputVal{
				word: "HAPPY",
			},
			want: 6,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumDistance(tt.args.word); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minimumDistance() = %v, want %v", got, tt.want)
			}
		})
	}
}
